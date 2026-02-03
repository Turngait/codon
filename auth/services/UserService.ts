import User from "../models/usersModelSQL";
import Tokens from "../models/tokensModelSQL";
import { dateNow } from "../utils/date";
import { createPassword, createPaper, createToken } from "../utils/sec";

export default class UserService {
  async addUser(email: string, pass: string): Promise<{ token: string | null; user_id: number | null, err: number | null; }>{
    const oldUser = await this.getUserByEmail(email);
    
    if (oldUser) return {token: null, user_id: null, err: 1};

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
      const dt = new Date()
      await Tokens.create({
        user_id: new_user.id,
        token: token,
        active_til: dt.setDate(dt.getDate() + 30)
      })

      return {token: token, user_id: new_user.id, err: null};
    } catch(err) {
      console.log(err);
      return {token: null, user_id: null, err: 5000};
    }
  }

  async signIn(email: string, pass: string): Promise<{ token: string | null; err: number | null; }> {
    try {
      const user = await this.getUserByEmail(email);
      
      if (!user) return {token: null, err: 4003};
      const userPass = createPassword(pass, user.paper);

      if (userPass === user.pass) {
        const token = createToken();
        const dt = new Date()
        await Tokens.create({
          user_id: user.id,
          token: token,
          active_til: dt.setDate(dt.getDate() + 30)
        })

        return {token, err: null};
      }
      
      return {token: null, err: 4003};
    
    } catch(err) {
      console.log(err);
      return {token: null, err: 5000};
    }
  }

  async getUserInfoByToken(token: string): Promise<{ user_id: string| null; email: string| null; token: string | null; }> {
    const token_data = await this.getToken(token);
    if (token_data) {
      const user_data = await this.getUserById(token_data.user_id);

      return user_data ? {user_id: token_data.user_id, email: user_data.email, token} : {user_id: token_data.user_id, email: null, token};

    }
    else return {user_id: null, email: null, token};
  }

  async changeUserPass(user_id: number, oldPass: string, newPass: string): Promise<{ isChanged: boolean | null; err: number | null; }> {
    const user_data = await this.getUserById(user_id);
    let userPassHash = createPassword(oldPass, user_data.paper);
    if (userPassHash === user_data.pass) {
      userPassHash = createPassword(newPass, user_data.paper);
      user_data.pass = userPassHash
      await user_data.save()
      return {isChanged: true, err: null};
    }

    return {isChanged: false, err: 4003};
  }

  async getUserByEmail(email: string) {
    return await User.findOne({where: {email}});
  }

  async getToken(token: string): Promise<any> {
    return await Tokens.findOne({where: {token}});
  }

  async getUserById(id: number): Promise<any> {
    return await User.findOne({where: {id}});
  }
}