import { NgModule } from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";

import {MainInterceptor} from "./main.interceptor";



@NgModule({
  declarations: [],
  imports: [
    HttpClientModule,
  ],
  exports: [
    HttpClientModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      multi: true,
      useClass: MainInterceptor
    }
  ]
})
export class HttpModule { }
