import { NextFunction, Request, Response } from 'express';

export default function validateChangePass (req: Request, res: Response, next: NextFunction) {
  if ((req.body.user_id && typeof req.body.user_id === 'number') 
      && (req.body.oldPass && typeof req.body.oldPass === 'string') 
    && (req.body.newPass && typeof req.body.newPass === 'string')) {
    next()
  }
  else {
    res.sendStatus(400)
  }
}