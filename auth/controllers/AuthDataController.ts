import { Request, Response } from 'express';
import UserService from '../services/UserService';

export default class AuthDataController {
    static async changePass(req: Request, res: Response) {
      const user = new UserService();
      try {
        const user_info = await user.changeUserPass(req.body.user_id, req.body.oldPass, req.body.newPass);
        if (user_info.isChanged) {
          return res.json({status: 200, msg: "pass is changed", data: null});
        } else if(user_info.err === 4003) {
          return res.json({status: 4003, msg: "old pass not match", data: null});
        }
        else {
          return res.json({status: 4004, msg: "user does not exist", data: null});
        }
      } catch(err) {
        return res.json({status: 5000, msg: "server error", data: null});
      }
    }
}