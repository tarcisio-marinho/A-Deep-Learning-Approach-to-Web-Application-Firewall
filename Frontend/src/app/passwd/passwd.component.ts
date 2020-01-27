import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { PasswdService } from './passwd.services';
import { THIS_EXPR } from '@angular/compiler/src/output/output_ast';
import { HttpClientModule, /* other http imports */ } from "@angular/common/http";
import Swal from 'sweetalert2';


@Component({
  selector: 'app-passwd',
  templateUrl: './passwd.component.html',
  styleUrls: ['./passwd.component.scss']
})
export class PasswdComponent implements OnInit {
  wordlist: any;
  forms: FormGroup;
  @ViewChild("cript", {static: false}) criptField: ElementRef;

  constructor(private passwdService: PasswdService) { 
    this.forms = new FormGroup({
      'passwd': new FormControl('')
    })
  }

  ngOnInit() {
  }

  sendToServer(payload){
    let send = {
      data:[payload['passwd']]
    }
    this.passwdService.Send(send).subscribe((ret: any) => {
      Swal.fire(ret['data'][0])
    });
  }
}
