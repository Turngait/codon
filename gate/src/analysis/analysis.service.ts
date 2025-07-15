import { Injectable } from '@nestjs/common';
import URI from '../config/uri';
import { AnalysisDTO, AnalysisGroupDTO } from './analysis.dto';

@Injectable()
export class AnalysisService {
  async addAnalysis(user_id: string, analysis: AnalysisDTO) {
    const result = await fetch(URI.CONS_URL + 'analysis', {
      method: 'POST',
      body: JSON.stringify({ user_id, ...analysis }),
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

  async getAnalysis(user_id: string) {
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

  async deleteAnalysis(user_id: string, analysis_id: string) {
    return await fetch(URI.CONS_URL + 'analysis', {
      method: 'DELETE',
      body: JSON.stringify({ user_id, analysis_id }),
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

  async updateAnalysis(user_id: string, analysis: AnalysisDTO) {
    return await fetch(URI.CONS_URL + 'analysis', {
      method: 'PUT',
      body: JSON.stringify({ user_id, ...analysis }),
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

  async addGroup(user_id: string, analysis: AnalysisGroupDTO) {
    const result = await fetch(URI.CONS_URL + 'analysis_groups', {
      method: 'POST',
      body: JSON.stringify({ user_id, ...analysis }),
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

  async delGroup(user_id: string, group_id: string) {
    const result = await fetch(URI.CONS_URL + 'analysis_groups', {
      method: 'DELETE',
      body: JSON.stringify({ user_id, group_id }),
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

  async updateGroup(user_id: string, analysis: AnalysisGroupDTO) {
    const result = await fetch(URI.CONS_URL + 'analysis_groups', {
      method: 'PUT',
      body: JSON.stringify({ user_id, ...analysis }),
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
