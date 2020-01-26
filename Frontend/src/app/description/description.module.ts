import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { DescriptionComponent } from './description.component';


@NgModule({
  declarations: [
    DescriptionComponent
  ],
  imports: [
    CommonModule,
    BrowserModule,
  ],
  exports: [DescriptionComponent]
})
export class DescriptionModule { }
