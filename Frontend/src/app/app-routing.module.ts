import { DashboardComponent } from './dashboard/dashboard.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  { path: '', redirectTo: 'inicio', pathMatch: 'full' },
  { path: 'inicio', component: DashboardComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes) ],
  
  exports: [RouterModule]
})
export class AppRoutingModule { }
