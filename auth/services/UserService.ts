import User from "../models/usersModelSQL";
import Tokens from "../models/tokensModelSQL";
import { dateNow } from "../utils/date";
import { createPassword, createPaper, createToken } from "../utils/sec";

export default class UserService {
  async addUser(email: string, pass: string): Promise<{ token: string | null; err: number | null; }>{
    const oldUser = await this.getUserByEmail(email);
    
    if (oldUser) return {token: null, err: 1};

    const paper = createPaper();
    try {
      const userDB = User.build({
        email: email,
        pass: createPassword(pass, paper),
        paper: paper,
        createdAt: dateNow()
      })
      const new_user = await userDB.save();

      const token = createToken();
      
      await Tokens.create({
        user_id: new_user.id,
        token: token,
        active_til: Date.now()
      })

      return {token: token, err: null};
    } catch(err) {
      console.log(err);
      return {token: null, err: 5000};
    }
  }

  async signIn(email: string, pass: string): Promise<{ token: string | null; err: number | null; }> {
    try {
      console.log(email)
      const user = await this.getUserByEmail(email);
      console.log(user);
      
      if (!user) return {token: null, err: 4003};
      const userPass = createPassword(pass, user.paper);

      if (userPass === user.pass) {
        const token = createToken();
        await Tokens.create({
          user_id: user.id,
          token: token,
          active_til: Date.now()
        })

        return {token, err: null};
      }
      
      return {token: null, err: 4003};
    
    } catch(err) {
      console.log(err);
      return {token: null, err: 5000};
    }
  }

  async getUserByEmail(email: string) {
    return await User.findOne({where: {email}})
  }

  async getToken(token: string): Promise<any> {
    return await Tokens.findOne({where: {token}});
  }
}