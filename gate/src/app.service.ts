import { Injectable } from '@nestjs/common';
// import mongoose from 'mongoose';
// const { Schema } = mongoose;
import URI from './config/uri';

@Injectable()
export class AppService {
  getHello(): string {
    // mongoose.connect('mongodb://operator:example@mongo:27017/codon');
    // const catSchema = new Schema({ name: String });
    // const Cat = mongoose.model('Cat', catSchema);
    // const kitty = new Cat({ name: 'Zildjian' });
    // kitty.save().then(() => console.log('meow'));
    return 'Hello World!';
  }

  async getAllInfoForUser(user_id: number) {
    const homeostasis = await fetch(URI.HMS_URL + 'analysis/user', {
      method: 'POST',
      body: JSON.stringify({ user_id }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        return res.status;
      }
    });
    const genome = await fetch(URI.USERS_URL + 'getdata', {
      method: 'POST',
      body: JSON.stringify({ user_id }),
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      if (res.status == 200) {
        return res.json();
      } else {
        console.log(res.status);
        return res.status;
      }
    });
    console.log(genome);

    const data = {
      status:
        homeostasis &&
        homeostasis.status &&
        homeostasis.status &&
        homeostasis.status === 200 &&
        genome &&
        genome.status &&
        genome.status === 200
          ? 200
          : 500,
      services_status: {
        homeostasis:
          homeostasis && homeostasis.status && homeostasis.status === 200
            ? 'Ok'
            : 'Ko',
        genome: genome ? 'Ok' : ' Ko',
      },
      homeostasis: homeostasis ? homeostasis : null,
      genome: genome ? genome : null,
    };
    return data;
  }
}
