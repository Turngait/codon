import { Injectable } from '@nestjs/common';
import URI from '../config/uri';

@Injectable()
export class ClinicsService {
  async addClinic(user_id: number, clinic) {
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

  async deleteClinic(user_id: number, clinic_id: number) {
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

  async updateClinic(user_id: number, clinic) {
    const result = await fetch(URI.CONS_URL + 'clinic', {
      method: 'PUT',
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

  async addClinicPhone(user_id: number, clinicPhone) {
    const result = await fetch(URI.CONS_URL + 'clinic/phone', {
      method: 'POST',
      body: JSON.stringify({ user_id, ...clinicPhone }),
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

  async updateClinicPhone(user_id: number, clinic_phone) {
    const result = await fetch(URI.CONS_URL + 'clinic/phone', {
      method: 'PUT',
      body: JSON.stringify({ user_id, ...clinic_phone }),
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

  async deleteClinicPhone(user_id: number, id: number) {
    const result = await fetch(URI.CONS_URL + 'clinic/phone', {
      method: 'DELETE',
      body: JSON.stringify({ user_id, id }),
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

  async addClinicAddress(user_id: number, data) {
    const result = await fetch(URI.CONS_URL + 'clinic/address', {
      method: 'POST',
      body: JSON.stringify({ user_id, ...data }),
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

  async updateClinicAddress(user_id: number, clinic_address) {
    const result = await fetch(URI.CONS_URL + 'clinic/address', {
      method: 'PUT',
      body: JSON.stringify({ user_id, ...clinic_address }),
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

  async deleteClinicAddress(user_id: number, id: number) {
    const result = await fetch(URI.CONS_URL + 'clinic/address', {
      method: 'DELETE',
      body: JSON.stringify({ user_id, id }),
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
