import { Injectable } from '@nestjs/common';

import URI from '../config/uri';

@Injectable()
export class UserService {
  async getUserInfo(user_id: string): Promise<any> {
    let status = 200;
    const data = {
      user_data: null,
      analysis: null,
    };
    try {
      const user_data = await this.getUserDataById(user_id);
      const analysis = await this.getAnalysisForUser(user_id);
      if (
        user_data.status &&
        user_data.status == 200 &&
        analysis.status &&
        analysis.status == 200
      ) {
        data.user_data = user_data.data;
        data.analysis = analysis.data;
      } else {
        status = 400;
      }
    } catch {
      status = 500;
    }
    return { status, data };
  }

  async updateUserData(
    user_id,
    biological_gender,
    data_birth,
    weight,
    height,
  ): Promise<any> {
    const result = await fetch(URI.USERS_URL + 'updateuserdata', {
      method: 'PUT',
      body: JSON.stringify({
        user_id,
        biological_gender,
        data_birth,
        weight,
        height,
      }),
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

  async changeTimeZone(user_id: number, newTimeZone: string) {
    console.log(user_id);
    console.log(newTimeZone);

    return true;
  }

  async getAllDataForUser(email: string) {
    const data = await this.getUserDataById(email);

    return data;
  }

  async getUserDataById(user_id) {
    return await fetch(URI.USERS_URL + 'getdata', {
      method: 'POST',
      body: JSON.stringify({ user_id }),
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

  async getAnalysisForUser(user_id: string) {
    return await fetch(URI.CONS_URL + 'analysis/user', {
      method: 'POST',
      body: JSON.stringify({ user_id }),
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
