import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { DocumentoResponse } from '../models/documento.response';
import { DocumentoRequest } from '../models/documento.request';

@Injectable({
  providedIn: 'root'
})

export class DocumentoService {

  private readonly url = 'http://localhost:8000/documents';

  constructor(
    private readonly httpClient: HttpClient
  ) { }

  public listarDocumentos() : Observable<Array<DocumentoResponse>> {
    return this.httpClient.get<Array<DocumentoResponse>>(this.url);
  }

  public salvarDocumento(request: DocumentoRequest) : Observable<DocumentoResponse> {
    return this.httpClient.post<DocumentoResponse>('http://localhost:8000/document/create/', request)
  }

  public editarDocumento(request: DocumentoRequest) : Observable<DocumentoResponse> {
    return this.httpClient.patch<DocumentoResponse>(this.url+ '/' + request.id, request)
  }

  public excluirDocumento(id: number) : Observable<DocumentoResponse> {
    return this.httpClient.delete<DocumentoResponse>(this.url + '/' + id);
  }
}
