import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PasswdComponent } from './passwd/passwd.component';


const routes: Routes = [
  {path:'', component:PasswdComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
