import { Sell } from './../models/sell';
import { Detail } from './../models/detail';
import { Client } from './../models/client';
import { Product } from './../models/product';
import { ApiService } from './../servicios/api/api.service';
import { Component, OnInit, ViewChild} from '@angular/core';
import { Table } from 'primeng/table';
import { ToastService } from '../servicios/toast.service';
import { PrimeNGConfig } from 'primeng/api';


export class AppModule {}

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  products: Product[] = []
  clients: Client[] = []
  selectedProduct: Product = {} as Product;
  productsaux:Product[] = []
  selectedClient: Client = {} as Client;
  selectedDetail:Detail = {} as Detail;
  newClient:Client={} as Client;
  selectedSale:Sell = {} as Sell;
  amount: number = 1
  sellDetail: Detail[] = []
  detaild:Detail={} as Detail;
  sales: Sell[] = []
  displaySalesDetail: boolean = false;
  fecha = new Date()
 
  @ViewChild('dt') dt: Table | undefined;
  @ViewChild('dt2') dt2: Table | undefined;
  @ViewChild('dt3') dt3: Table | undefined;
  constructor(private api: ApiService, private toastService: ToastService , private primengConfig: PrimeNGConfig


    ) {

  }
  ngOnInit(): void {
    this.selectedProduct.marca = ""
    this.getAllClients()
    this.getAllProducts()
    this.getAllSales()
    //this.getDateBDSQL()
    setInterval(()=>{
     this.fecha = new Date()
   },1000)
    this.primengConfig.ripple = true;
  }

  display: boolean = false;
  showDialog() {
      this.display = true;
  }

  applyFilterGlobal($event: any, stringVal: any) {
    this.dt?.filterGlobal(($event.target as HTMLInputElement).value, stringVal);
  }
  applyFilterGlobalClient($event: any, stringVal: any) {
    this.dt2?.filterGlobal(($event.target as HTMLInputElement).value, stringVal);
  }
  applyFilterGlobalSell($event: any, stringVal: any) {
    this.dt3?.filterGlobal(($event.target as HTMLInputElement).value, stringVal);
  }

  onProductSelect(event: any) {
   
      this.selectedProduct = event.data
   
    
  }

  onClientSelect(event: any) {
    this.selectedClient = event.data
  }
  onSellSelect(event: any) {
    this.selectedClient = event.data
  }

  getAllClients() {

    this.api.getAllClients().subscribe(data => {
      this.clients = data
    },error=>{

      error.message = "No se obtuvieron resultados"
      this.toastService.showError('Error', error.message)
    }
    )
    
  }

  getAllProducts() {
    this.api.getAllProducts().subscribe(data => {
      this.products = data
    },error=>{

      error.message = "No se obtuvieron resultados"
      this.toastService.showError('Error', error.message)
    }
    )
  }

/*
  getDateBDSQL()
  {
    this.api.getDateBDS().subscribe(data=>{ 

      data.forEach(x=>{
        this.fecha= new Date(x.fechaRegistro);
      })
    },error=>{
      error.message = "No hubo resultados"
      this.toastService.showError('Error', error.message)
    }
    )
  }
*/



   getAllSales() {
     this.api.getSales().subscribe(data => {
       data.forEach(x=>{
         this.api.getDetailsId(x.idVenta!).subscribe(datad=>{
           x.detalles=datad
         })
       })
       this.sales = data
     },error=>{
       error.message = "No se obtuvieron resultados"
       this.toastService.showError('Error', error.message)
     }
     )
   }

  
  
  
 
  addDetail(product: Product) {
    if (!product.idCategoria) {
      this.toastService.showWarn('Error', 'Debes seleccionar un producto')
    } else

  {
     let detail: Detail = {
        idProducto: product.idProducto,
        cantidad: this.amount,
        marcaProducto: product.marca,
        precio: product.precio,
        categoriaProducto: product.idCategoria.toString(),
        descripcionProducto: product.descripcion
      }
     this.productsaux.push(product)


const i = this.sellDetail.findIndex(_element => _element.idProducto === detail.idProducto);
      if (i > -1) {
        this.sellDetail[i] = detail
        this.toastService.showInfo('Aviso', 'El producto ya fué seleccionado')
      }
      else if (detail.cantidad>product.stock)
      {
        this.toastService.showInfo('Aviso', 'El valor debe ser menor o igual al stock')
      }
      else if (detail.cantidad==0 || detail.cantidad.toString().valueOf()=='')
      {
        this.toastService.showInfo('Aviso', 'El valor debe ser mayor a 0')
      }
      else 
      {
        this.sellDetail.push(detail);

    
        
      }

    }
 
  }

  addClient(clients:Client) { 

      let client : Client = {
        nombre : clients.nombre,
        cedula : clients.cedula,
        correo: clients.correo,
        telefono : clients.telefono,
        fechaRegistro : new Date()
        }
        if (client.nombre=="" || client.cedula==""
        || client.correo=="" || client.telefono=="" ||
        client.fechaRegistro=="")
        {
        this.toastService.showWarn('Error',"Debes completar todos los campos porfavor !")
        }
        else{
          this.api.createClient(client).subscribe(()=>{
            this.newClient={} as Client;
            this.toastService.showSuccess('Éxito', 'Cliente agregado')
            this.getAllClients()
        },error=>
    
        {
          error.message = "Debes completar todos los campos"
           this.toastService.showWarn('Error',error.message)
        }
    
        )
        }
}

 validaNumericos(event:any) {
  if(event.charCode >= 48 && event.charCode <= 57){
    return true;
   }
   return false;        
}

  calculateSubtotal(details: Detail[]): number {
    let total = 0
    details.forEach(detail => {
      total += detail.cantidad * detail.precio
    })
    return total
  }
  calculateIva(details: Detail[]): number {
    let total = 0
    details.forEach(detail => {
      total += detail.cantidad * detail.precio
    })
    return total * 0.12
  }
  calculateTotal(details: Detail[]): number {
    let total = 0
    details.forEach(detail => {
      total += detail.cantidad * detail.precio
    })
    return total + total * 0.12
  }
validardetail(details:Detail[], products:Product[]):boolean{
  let  bol = true
      details.forEach(detail=>{
         products.forEach(product=>{
             if(detail.cantidad>product.stock || detail.cantidad==0 || detail.cantidad.toString().valueOf()=='')
             bol=false
         })
      })
   return bol
}

  sell(details: Detail[], client: Client ) {
   if(!this.validardetail(details,this.productsaux))
   {
    this.toastService.showInfo('Aviso', 'El valor debe ser menor o igual al stock ')
   }
   else
   {

    let sell: Sell = {
      numeroVenta: "ven",
      idCliente: client.idCliente!,
      subTotal: this.calculateSubtotal(details),
      impuestoTotal: this.calculateIva(details),
      Total: this.calculateTotal(details),
     fechaRegistro: new Date(),
      nombre:client.nombre,
      cedula:client.cedula,
      telefono:client.telefono
    }
            this.api.createSell(sell).subscribe(() => {
              details.forEach(detail => {
                let detailToSave: Detail = {
                  cantidad: detail.cantidad,
                  categoriaProducto: detail.categoriaProducto,
                  descripcionProducto: detail.descripcionProducto,
                  idProducto: detail.idProducto,
                  marcaProducto: detail.marcaProducto,
                  precio: detail.precio,
                  total: detail.precio * detail.cantidad
                }
                this.api.createDetail(detailToSave).subscribe(()=>{
                  this.getAllProducts()
                })
              })
              this.toastService.showSuccess('Éxito', 'Venta generada')
              this.getAllSales()
            },error=>{
  
              error.message = "No se pudo crear la venta"
  
              this.toastService.showError('Error', error.message)
            }
            )
            this.selectedProduct = {} as Product
            this.selectedClient = {} as Client
            this.amount = 1
            this.sellDetail = []

   }
  
  }
    

  removeProduct(productId: number) {
    this.sellDetail = this.sellDetail.filter(product => {
      return product.idProducto !== productId;
    })
  }

}
