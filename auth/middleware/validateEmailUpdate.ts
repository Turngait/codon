import { NextFunction, Request, Response } from 'express';

export default function validateEmailUpdate (req: Request, res: Response, next: NextFunction) {
  if ((req.body.user_id && typeof req.body.user_id === 'number') 
      && (req.body.email && typeof req.body.email === 'string')) {
    next()
  }
  else {
    res.sendStatus(400)
  }
}