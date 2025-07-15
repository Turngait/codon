import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

import ApiAuth from 'src/models/api_auth.model';

@Injectable()
export class CheckTokenMiddleware implements NestMiddleware {
  async use(req: Request, res: Response, next: NextFunction) {
    if (req.headers.token) {
      const apiEntity = await ApiAuth.findOne({
        apiToken: req.headers.token,
      }).exec();
      if (apiEntity) {
        next();
      } else {
        res.json({ status: 403, msg: 'Access denied' });
      }
    } else {
      res.json({ status: 403, msg: 'Access denied' });
    }
  }
}
