import { Injectable } from '@nestjs/common';
import { createHash } from 'crypto';
import ApiAuth from 'src/models/api_auth.model';
import { getToday, getTodayPlus30Days } from 'src/utils/date';

@Injectable()
export class ApiauthService {
  async generateAuthToken(
    contactEmail: string,
    clientName: string,
  ): Promise<any> {
    const oldEntity = await this.getTokensByClientEmail(contactEmail);
    if (oldEntity) {
      return {
        status: 200,
        msg: 'Token already exist. Please ask administrator to fetch token',
      };
    }
    const token = this.createToken(contactEmail);
    try {
      const apiAuthEntity = new ApiAuth({
        contactEmail,
        clientName,
        authToken: token,
        apiToken: null,
        activeTill: getTodayPlus30Days(),
        createdAt: getToday(),
      });
      await apiAuthEntity.save();
      return {
        status: 200,
        msg: 'Token successfully created. Please ask administrator to fetch token',
      };
    } catch (err) {
      console.log(err);
      return {
        status: 500,
        msg: 'Server error. Try again later',
      };
    }
  }

  async generateApiToken(authToken: string, contactEmail: string) {
    const clientEntity = await this.getTokensByClientEmail(contactEmail);
    try {
      if (clientEntity && clientEntity.authToken === authToken) {
        const token = this.createToken(contactEmail);
        clientEntity.apiToken = token;
        clientEntity.activeTill = getTodayPlus30Days();
        await clientEntity.save();
        return {
          status: 200,
          msg: 'Api token was created',
          token,
        };
      }
      return {
        status: 4003,
        msg: 'Client does not exist or wrong auth token',
      };
    } catch (err) {
      console.log(err);
      return {
        status: 500,
        msg: 'Server error. Try again later',
      };
    }
  }

  async getTokensByClientEmail(contactEmail: string): Promise<any> {
    return await ApiAuth.findOne({ contactEmail }).exec();
  }

  createToken(email: string): string {
    return createHash('sha256')
      .update(email + String(Date.now()))
      .digest('hex');
  }
}
