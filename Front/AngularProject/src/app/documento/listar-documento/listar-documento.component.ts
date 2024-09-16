import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { DocumentoResponse } from '../models/documento.response';
import { EmpresaResponse } from '../models/empresa.response';
import { EmpresaService } from '../services/empresa.service';
import { DocumentoService } from '../services/documento.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-listar-documento',
  templateUrl: './listar-documento.component.html'
})

export class ListarDocumentoComponent implements OnInit {
  public documentoResponse = new Array<DocumentoResponse>();
  public empresaResponse = new Array<EmpresaResponse>();

  constructor(
    private readonly documentosService: DocumentoService,
    private readonly empresaService: EmpresaService,
    private readonly toastr: ToastrService,
    private readonly router: Router
  ) { }

  ngOnInit(): void {
    this.listarDocumentos();
    this.listarEmpresas();
  }

  public listarDocumentos() {
    this.documentosService
      .listarDocumentos()
      .subscribe(response => {
        this.documentoResponse = response;
      });
  }

  public listarEmpresas() {
    this.empresaService
      .listarEmpresas()
      .subscribe(response => {
        this.empresaResponse = response;
      });
  }

  public excluirDocumento(documento: DocumentoResponse) {
    this.documentosService
      .excluirDocumento(documento.id)
      .subscribe(response => {
        this.toastr.success('Sucesso!', 'O documento '+ documento.name +' foi excluído');
        this.listarDocumentos();
      }, erro => {
        this.toastr.error('Erro!', 'O documento '+ documento.name +' não foi excluído');
      }
    );
  }

  public editarDocumento(documento: DocumentoResponse) {
    this.router.navigate(['/cadastrar-documento'], { state: { data: documento } });
  }
}
