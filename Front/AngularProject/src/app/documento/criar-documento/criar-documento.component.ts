import { Component, inject, OnInit } from '@angular/core';
import { finalize } from 'rxjs';
import { DocumentoRequest } from '../models/documento.request';
import { FormArray, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Signatario } from '../models/signatario';
import { DocumentoService } from '../services/documento.service';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';
import { SignatarioService } from '../services/signatario.service';

@Component({
  selector: 'app-criar-documento',
  templateUrl: './criar-documento.component.html'
})

export class CriarDocumentoComponent implements OnInit {
  private formBuilder = inject(FormBuilder);
  public documentoForm: FormGroup;

  public nomeArquivo = '';

  public documentoRequest?: DocumentoRequest;
  public listaSignatarios = new Array<Signatario>();
  public signatariosRemovidos = new Array<Signatario>();

  constructor(
    private readonly documentosService: DocumentoService,
    private readonly signatariosService: SignatarioService,
    private readonly spinner: NgxSpinnerService,
    private readonly toastr: ToastrService,
    private readonly router: Router
  ) {
    this.documentoForm = this.formBuilder.group({
      arquivo: [ '', Validators.required ],
      nomeResponsavel: ['', Validators.required],
      signatarios: this.formBuilder.array([])
    });
  }

  ngOnInit(): void {
    this.documentoRequest = history.state.data as DocumentoRequest;
    this.inicializarFormulario();
  }

  public inicializarFormulario() {
    this.documentoForm = this.formBuilder.group({
      id: [ this.documentoRequest?.id || 0 ],
      arquivo: [ '', Validators.required ],
      nomeResponsavel: [ this.documentoRequest?.created_by || '', Validators.required ],
      signatarios: this.formBuilder.array([])
    });

    if (this.documentoRequest) {
      this.nomeArquivo = this.documentoRequest.name;
      this.documentoForm.patchValue({
        arquivo: this.nomeArquivo
      });

      this.recuperarSignatarios();
    }
  }

  private recuperarSignatarios() {
    this.signatariosService
      .recuperarSignatariosDoDocumento(this.documentoRequest?.id || 0)
      .subscribe(response => {
        this.listaSignatarios = response;
        this.inicializarFormularioSignatario();
      }
    );
  }

  private inicializarFormularioSignatario() {
    const signatariosFormArray = this.documentoForm.get('signatarios') as FormArray;

    this.listaSignatarios.forEach(signatario => {
      const signatarioFormGroup = this.formBuilder.group({
        id: [ signatario.id ],
        name: [ signatario.name || '', Validators.required],
        email: [ signatario.email || '', Validators.required],
      });

      signatariosFormArray.push(signatarioFormGroup);
    });
  }

  public abrirExplorerArquivos() {
    document.getElementById('explorer-arquivo')?.click();
  }

  public adicionarArquivo(evento: Event) {
    const target = evento.target as HTMLInputElement;
    const arquivosSelecionados = target.files!.item(0);
    this.nomeArquivo = arquivosSelecionados!.name;

    this.documentoForm.patchValue({
      arquivo: this.nomeArquivo
    });
  }

  public adicionarSignatario() {
    const novoSignatario = this.formBuilder.group({
      id: [ 0 ],
      name: [ '', Validators.required ],
      email: [ '', Validators.required ]
    })

    return (this.documentoForm.get('signatarios') as FormArray).push(novoSignatario);
  }

  public removerSignatario(index: number) {
    if (this.listaSignatarios) {
      this.signatariosRemovidos.push(this.listaSignatarios[index])
    }

    return (this.documentoForm.get('signatarios') as FormArray).removeAt(index);
  }

  get signatarios() {
    return (this.documentoForm.get('signatarios') as FormArray).controls as FormGroup[];
  }

  public salvarDocumento() {
    this.spinner.show();

    var request = new DocumentoRequest({
      name: this.nomeArquivo,
      created_by: this.documentoForm.get('nomeResponsavel')?.value || "",
      signatarios: this.documentoForm.get('signatarios')!.value as Array<Signatario>
    });

    if (this.documentoRequest) {
      this.editarDocumento(request)
    } else {
      this.criarDocumento(request);
    }

  }

  private criarDocumento(request: DocumentoRequest) {
    this.documentosService
      .salvarDocumento(request)
      .pipe(finalize(() => {
        setTimeout(() => {
          this.spinner.hide();
          this.router.navigate(['/listar-documento']);
        }, 1000);
      }))
      .subscribe(response => {
        this.toastr.success('Sucesso!', 'Documento foi criado!');
      }, erro => {
        this.toastr.error('Erro!', 'O documento não foi salvo');
      }
    );
  }

  private editarDocumento(request: DocumentoRequest) {

    request.id = this.documentoRequest?.id;
    if (this.signatariosRemovidos) {
      request.signatariosRemovidos = this.signatariosRemovidos;
    }

    this.signatariosService
      .editarSignatarios(request)
      .pipe(finalize(() => {
        setTimeout(() => {
          this.spinner.hide();
          this.router.navigate(['/listar-documento']);
        }, 1000);
      }))
      .subscribe(response => {
        this.toastr.success('Sucesso!', 'Signatario foi editado!');
      }, erro => {
        this.toastr.error('Erro!', 'O documento não foi editado');
      }
    );
  }

  public limparFormulario() {
    this.documentoForm.reset();
    const signatariosFormArray = this.documentoForm.get('signatarios') as FormArray;
    signatariosFormArray.clear();
  }

  public cancelar() {
    this.router.navigate(['/listar-documento']);
  }
}
