import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';


@Injectable()
export class PasswdService{
   
    private URL: String = environment.URL;

    constructor(private http: HttpClient) { }

    Send(payload): Observable<any> {
        return this.http.post<any>(this.URL + "predict", payload);
    }
}