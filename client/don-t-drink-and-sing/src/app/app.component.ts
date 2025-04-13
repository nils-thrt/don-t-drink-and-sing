

import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: "./app.component.html"
})
  
export class AppComponent {

  constructor(private http: HttpClient) { }
  
  private upcomingTracks = [
    { name: 'Track 1' },
    { name: 'Track 2' },
    { name: 'Track 3' },]

  login() {
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };
    this.http.post('http://localhost:3000/api/login', { username: 'admin', password: 'admin' }, httpOptions)
      .subscribe((response) => {
        console.log(response);
      }, (error) => {
        console.error(error);
      });
  }
}
