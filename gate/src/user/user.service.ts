import { Injectable } from '@nestjs/common';

import URI from '../config/uri';

@Injectable()
export class UserService {
  async getUserInfo(email): Promise<any> {
    const data = await this.getUserDataByEmail(email);
    if (data.status && data.status == 200) {
      return { status: 200, data: data.data };
    } else {
      return { status: 403, data: null };
    }
  }

  async updateUserData(email, data): Promise<any> {
    const result = await fetch(URI.USERS_URL + 'updatedata', {
      method: 'PUT',
      body: JSON.stringify({ email, data }),
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

  async getUserDataByEmail(email) {
    return await fetch(URI.USERS_URL + 'getdata', {
      method: 'POST',
      body: JSON.stringify({ email }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        console.log(res.status);
        return res.status;
      }
    });
  }
}
