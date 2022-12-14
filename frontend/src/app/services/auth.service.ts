import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {IToken, IUser} from "../interfaces";
import {Observable} from "rxjs";
import {urls} from "../constants";

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private  accessTokenKey = 'access'

  constructor(private httpClient: HttpClient) {
  }

  register(user: IUser): Observable<IUser> {
    return this.httpClient.post<IUser>(urls.users, user)
  }

  login(user: IUser): Observable<IToken> {
    return this.httpClient.post<IToken>(urls.auth, user)
  }

  setToken(token: IToken): void {
    return localStorage.setItem(this.accessTokenKey, token.access)
  }

  getToken(): string {
    return localStorage.getItem(this.accessTokenKey) as string
  }

  deleteToken(): void {
    localStorage.removeItem(this.accessTokenKey)
  }

  isAuthorized(): boolean {
    return !!localStorage.getItem(this.accessTokenKey)
  }

}
