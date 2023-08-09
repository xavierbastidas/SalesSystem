import { Detail } from "./detail";

export interface Sell {
    idVenta?:number,
    numeroVenta:any,
    idCliente:number,
    subTotal:number,
    impuestoTotal:number,
    Total:number,
    fechaRegistro:any,
    nombre:string,
    cedula:string,
    detalles?:Detail[]
    telefono:string
}
