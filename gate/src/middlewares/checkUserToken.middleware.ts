import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import URI from '../config/uri';

@Injectable()
export class CheckUserTokenMiddleware implements NestMiddleware {
  async use(req: Request, res: Response, next: NextFunction) {
    console.log(req.headers.user_token);
    if (!req.headers.user_token)
      res.json({ status: 403, msg: 'Wrong user token' });

    const response = await this.getInfoFromAuthApi(req.headers.user_token);
    if (response && response.status === 200) {
      req.headers.user_email = response.data.userInfo.email;
      req.headers.user_id = response.data.userInfo.user_id;
      next();
    } else {
      res.json({ status: 403, msg: 'Wrong user token' });
    }
  }

  async getInfoFromAuthApi(token) {
    return await fetch(URI.AUTH_URL + 'getinfo', {
      method: 'POST',
      body: JSON.stringify({ token }),
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

  async getUserId(email) {
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
