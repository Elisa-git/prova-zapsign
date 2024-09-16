import { Signatario } from "./signatario";

export class DocumentoRequest {
  public id?: number;
  public name!: string;
  public status?: string;
  public created_by!: string;
  public signatarios: Array<Signatario>;
  public signatariosRemovidos?: Array<Signatario>;
  public companyId!: number;

  constructor(params: Partial<DocumentoRequest>) {
    this.id = params.id;
    this.name = params.name || '';
    this.status = params.status;
    this.created_by = params.created_by || '';
    this.signatarios = params.signatarios || [];
    this.signatariosRemovidos = params.signatariosRemovidos;
  }

}
