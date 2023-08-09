import { Detail } from './../../models/detail';
import { Client } from './../../models/client';
import { Product } from './../../models/product';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Sell } from 'src/app/models/sell';
import { Date } from 'src/app/models/date';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  apiUrl = "http://localhost:8000/"
  constructor(private http: HttpClient) { }

  getAllProducts(): Observable<Product[]>{
    return this.http.get<Product[]>(this.apiUrl+"products")
  }
  getAllClients(): Observable<Client[]>{
    return this.http.get<Client[]>(this.apiUrl+"customers")
  }
  createSell(sell:Sell){
    return this.http.post<Sell>(this.apiUrl+'sell',sell)
  }
   createClient(client:Client)
   {
    return this.http.post<Client>(this.apiUrl+"customers",client)
   }
  createDetail(detail:Detail){
    return this.http.post(this.apiUrl+'detail',detail)
  }
  getSales():Observable<Sell[]>{
    return this.http.get<Sell[]>(this.apiUrl+'sales')
  }


  getDetailsId(_idVenta:number):Observable<Detail[]>{
    return this.http.get<Detail[]>(this.apiUrl+'detail/'+_idVenta)
  }

   getDateBDS():Observable<Date[]>{

    return this.http.get<Date[]>(this.apiUrl+'date')
   }





 

}
