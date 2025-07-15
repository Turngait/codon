import { Injectable } from '@nestjs/common';
// import mongoose from 'mongoose';
// const { Schema } = mongoose;

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
}
