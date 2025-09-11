import { Injectable } from '@nestjs/common';
import fetch from 'node-fetch';

import URI from '../config/uri';

@Injectable()
export class AuthService {
  async signUp(
    email: string,
    pass: string,
    data: any,
    settings: any,
  ): Promise<any> {
    const statusFromAuthApi = await this.createUser(email, pass);
    if (
      statusFromAuthApi &&
      statusFromAuthApi.status &&
      statusFromAuthApi.status !== 200
    ) {
      return statusFromAuthApi;
    }
    await this.addUsersData(email, data, settings);

    return statusFromAuthApi;
  }

  async signIn(email: string, pass: string): Promise<any> {
    const result = await fetch(URI.AUTH_URL + 'signIn', {
      method: 'POST',
      body: JSON.stringify({ email, pass }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        return res.status;
      }
    });
    return result;
  }

  async createUser(email: string, pass: string): Promise<any> {
    const result = await fetch(URI.AUTH_URL + 'signUp', {
      method: 'POST',
      body: JSON.stringify({ email, pass }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        console.log(res.status);
        return res.status;
      }
    });
    return result;
  }

  async addUsersData(email, data, settings) {
    const result = await fetch(URI.USERS_URL + 'user', {
      method: 'POST',
      body: JSON.stringify({ email, data: data, settings: settings }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        console.log(res.status);
        return res.status;
      }
    });
    return result;
  }
}
