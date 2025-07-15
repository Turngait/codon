import User from "../models/userModel";
import { dateNow } from "../utils/date";
import { createPassword, createPaper, createToken } from "../utils/sec";

export default class UserService {
  async addUser(email: string, pass: string): Promise<{ token: string | null; err: number | null; }>{
    const oldUser = await this.getUserByEmail(email);
    if (oldUser) return {token: null, err: 1};

    const paper = createPaper();
    try {
      const newUser = new User({ 
        email: email,
        pass: createPassword(pass, paper),
        paper: paper,
        ips: [""],
        token: createToken(),
        createdAt: dateNow()
      });
      newUser.save();
      return {token: newUser.token ? newUser.token : null, err: null};
    } catch(err) {
      console.log(err);
      return {token: null, err: 5000};
    }
  }

  async signIn(email: string, pass: string): Promise<{ token: string | null; err: number | null; }> {
    try {
      const user = await this.getUserByEmail(email);
      
      if (!user) return {token: null, err: 4003};
      const userPass = createPassword(pass, user.paper);

      if (userPass === user.pass) {
        user.token = createToken();
        user.save();
        return {token: user.token, err: null};
      }
      return {token: null, err: 4003};
    } catch(err) {
      console.log(err);
      return {token: null, err: 5000};
    }


  }

  async getUserByEmail(email: string): Promise<any> {
    return await User.findOne({email}).exec();
  }

  async getUserInfoByToken(token: string): Promise<any> {
    return await User.findOne({token}).exec();
  }
}