import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CriarDocumentoComponent } from './documento/criar-documento/criar-documento.component';
import { ListarDocumentoComponent } from './documento/listar-documento/listar-documento.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'listar-documento',
    pathMatch: 'full'
  },
  {
    path: 'cadastrar-documento',
    component: CriarDocumentoComponent
  },
  {
    path: 'listar-documento',
    component: ListarDocumentoComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
