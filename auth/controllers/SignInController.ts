import { Request, Response } from 'express';
import UserService from '../services/UserService';


export default class SignInController {
  static async signIn(req: Request, res: Response) {
    const user = new UserService();
    const newUser = await user.signIn(req.body.email, req.body.pass);
    
    if (newUser && newUser.token) {
      res.json({status: 200, msg: "success", data: {token: newUser.token}});
    }
    else if (newUser && newUser.err && newUser.err === 4003) {
      res.json({status: 4003, msg: "incorrect password or email", data: {token: null}});
    }
    else {
      res.json({status: 5000, msg: "server error", data: {token: null}});
    }
  }
}
