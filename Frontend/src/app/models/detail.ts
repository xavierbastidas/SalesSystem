export interface Detail {
    idDetalleVenta?:number,
    idVenta?: number,
    idProducto?: number,
    marcaProducto: string,
    descripcionProducto:string,
    categoriaProducto:string,
    cantidad:number,
    precio:number,
    total?:number
}
