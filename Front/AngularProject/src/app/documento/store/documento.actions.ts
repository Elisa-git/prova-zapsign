import { createAction, props } from "@ngrx/store";
import { IDocumento } from "./documento.state";

export const loadListaDocumentos = createAction('[Documento] load lista documentos');
export const loadListaDocumentosSucesso = createAction(
  '[Documento] load lista documentos sucesso',
  props<{ entities: IDocumento[] }>()
)
export const loadListaDocumentosErro = createAction(
  '[Documento] load lista documentos sucesso'
)
