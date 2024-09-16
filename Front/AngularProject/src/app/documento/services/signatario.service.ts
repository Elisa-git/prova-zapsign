import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Signatario } from '../models/signatario';
import { DocumentoRequest } from '../models/documento.request';

@Injectable({
  providedIn: 'root'
})
export class SignatarioService {

  private readonly url = 'http://localhost:8000/';

  constructor(
    private readonly httpClient: HttpClient
  ) { }

  public recuperarSignatariosDoDocumento(idDocumento: number) : Observable<Array<Signatario>> {
    return this.httpClient.get<Array<Signatario>>(this.url + 'document/' + idDocumento + '/signers/');
  }

  // public editarSignatarios(request: Array<Signatario>) {
  public editarSignatarios(request: DocumentoRequest) {
    return this.httpClient.patch(this.url + 'signers/update/', request);
  }
}
