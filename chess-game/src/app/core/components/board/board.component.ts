import { Component, OnInit } from '@angular/core';

import { CoreService } from 'src/app/core/core.service';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.scss']
})
export class BoardComponent implements OnInit {
  showCircle = false;

  constructor(
    private coreService: CoreService
  ) { }

  ngOnInit(): void {
  }

  test() { 
    this.showCircle = !this.showCircle
    console.log(this.showCircle)
  }

}
