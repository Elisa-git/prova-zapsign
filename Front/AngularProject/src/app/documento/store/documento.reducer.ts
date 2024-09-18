import { createReducer, on } from "@ngrx/store";
import { IDocumentoState } from "./documento.state";
import { loadListaDocumentos, loadListaDocumentosErro, loadListaDocumentosSucesso } from "./documento.actions";

export const initialState: IDocumentoState = {
  entities: [],
  isLoading: false
}

export const documentosReducer = createReducer(
  initialState,
  on(loadListaDocumentos, (state) => ({
    ...state,
    isLoading: true
  })),
  on(loadListaDocumentosSucesso, (state, { entities }) => ({
    ...state,
    entities,
    isLoading: false
  })),
  on(loadListaDocumentosErro, (state) => ({
    ...state,
    isLoading: false
  })),
)
