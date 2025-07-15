import { NextFunction, Request, Response } from 'express';

export default function validateGetUserInfo (req: Request, res: Response, next: NextFunction) {
  if (req.body.token && typeof req.body.token === 'string') {
    next()
  }
  else {
    res.sendStatus(400)
  }
}