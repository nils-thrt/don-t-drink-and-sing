
import { Component } from '@angular/core';
import { HttpClient, HttpClientModule, HttpHeaders } from '@angular/common/http';
import { Consts } from  "../app-config";



import { ServerResponse } from 'http';
import { log } from 'console';

@Component({
  selector: "app-component",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css", "../styles.css"],
  imports: [HttpClientModule],
})
export class AppComponent {

  constructor(private http: HttpClient) { }

  private upcomingTracks = [
    { name: 'Track 1' },
    { name: 'Track 2' },
    { name: 'Track 3' },]



    
/*   onload() {
    dddd
  }
   */

  ngAfterViewInit() {

    
  }






  anotherFunction() {
  
    
    const httpOptions = {
      headers: new HttpHeaders({ 
        'Content-Type': 'application/json',
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





