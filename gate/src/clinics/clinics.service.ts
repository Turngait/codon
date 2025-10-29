import { Injectable } from '@nestjs/common';
import URI from '../config/uri';

@Injectable()
export class ClinicsService {
  async addClinic(user_id, clinic) {
    const result = await fetch(URI.CONS_URL + 'clinic', {
      method: 'POST',
      body: JSON.stringify({ user_id, ...clinic }),
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

  async deleteClinic(user_id, clinic_id: number) {
    const result = await fetch(URI.CONS_URL + 'clinic', {
      method: 'DELETE',
      body: JSON.stringify({ user_id, clinic_id }),
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
