import { Request, Response } from 'express';
import UserService from '../services/UserService';


export default class SignUpController {
  static async signUp(req: Request, res: Response) {
    const user = new UserService();
    const newUser = await user.addUser(req.body.email, req.body.pass);
    
    if (newUser && newUser.token) {
      res.json({status: 200, msg: "user have created", data: {token: newUser.token}});
    }
    else if (newUser && newUser.err && newUser.err === 1) {
      res.json({status: 4013, msg: "user exist", data: {token: null}});
    }
    else {
      res.json({status: 5000, msg: "server error", data: {token: null}});
    }
  }
}
