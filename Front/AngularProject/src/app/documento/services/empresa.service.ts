import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EmpresaResponse } from '../models/empresa.response';

@Injectable({
  providedIn: 'root'
})

export class EmpresaService {

  private readonly url = 'http://localhost:8000/companies';

  constructor(
    private readonly httpClient: HttpClient
  ) { }

  public listarEmpresas() : Observable<Array<EmpresaResponse>> {
    return this.httpClient.get<Array<EmpresaResponse>>(this.url);
  }
}
