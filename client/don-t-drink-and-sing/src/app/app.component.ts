
import { Component, NgModule } from '@angular/core';
import { HttpClient, HttpClientModule, HttpHeaders, provideHttpClient, withNoXsrfProtection } from '@angular/common/http';
import { Consts } from  "../app-config";



import { ServerResponse } from 'http';
import { log } from 'console';

@Component({
  selector: "app-component",
  template: `
    
      
          <span>Upcoming Tracks</span>
          <button class="btn btn-primary" (click)="this.login()" type="button">Click me!</button>
   
 
  `,
  imports: [HttpClientModule],
  providers: [
    
  ]
})
export class AppComponent {

  constructor(private http: HttpClient) { }

  private upcomingTracks = [
    { name: 'Track 1' },
    { name: 'Track 2' },
    { name: 'Track 3' },]

  login() {
    console.log("Hello from login");
    const httpOptions = {
      headers: new HttpHeaders({ 
        'Content-Type': 'application/json',
        "Access-Control-Allow" : "*",
        // "Access-Control-Allow-Origin" : "*",
        "crossdomain": "true",
      })
    };
    this.http.get(Consts.SERVER_URL + "/login", httpOptions)
      .subscribe((response) => {
        console.log(response);
      }, (error) => {
        console.error(error);
      });
  }
}





