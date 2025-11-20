import { Request, Response } from 'express';
import UserService from '../services/UserService';

export default class UserInfoController {
  static async getUserInfo(req: Request, res: Response) {
    const user = new UserService();
    try {
      const user_info = await user.getUserInfoByToken(req.body.token);
      if (user_info && user_info.user_id && user_info.email) {
        return res.json({status: 200, msg: "user data granted", data: {userInfo: {user_id: user_info.user_id, email: user_info.email, token: user_info.token}}});
      } else {
        return res.json({status: 4013, msg: "user does not exist", data: {user_id: null, email:null, token: null}});
      }
    } catch(err) {
      return res.json({status: 5000, msg: "server error", data: {user_id: null, email:null, token: null}});
    }
  }
}