export interface IDocumento {
  id: number;
  name: string;
  status: number;
  created_by: string;
}

export interface IDocumentoState {
  entities: IDocumento[];
  isLoading: boolean;
}
