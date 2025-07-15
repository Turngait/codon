import { NextFunction, Request, Response } from 'express';

export default function validateSignIn (req: Request, res: Response, next: NextFunction) {
  console.log('Body:', req.body)
  if (req.body.email && req.body.pass && typeof req.body.pass === 'string' && typeof req.body.email === 'string') {
    next()
  }
  else {
    res.sendStatus(400)
  }
}