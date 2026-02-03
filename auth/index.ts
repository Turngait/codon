const express = require('express');

import mongoose from 'mongoose';
import 'dotenv/config'

import SignUpRouter from './routers/signup';
import SignInRouter from './routers/signin';
import GetUserInfoRouter from './routers/getuserinfo';
import ChangePassRouter from './routers/changePass';

import { APP_CONFIG } from './config/app.config';
import { MONGO_CONFIG } from './config/mongo.config';
import { connectToDB, sequelize } from './db';


const app = express();

app.use(express.json({
  inflate: true,
  strict: true,
  type: 'application/json'
}));


app.use('/signup', SignUpRouter)
app.use('/signin', SignInRouter)
app.use('/getinfo', GetUserInfoRouter)
app.use('/changePassword', ChangePassRouter)

app.listen(APP_CONFIG.PORT, async () => {
  console.log(`Server is running at https://localhost:${APP_CONFIG.PORT}`);
  // Add event for mongoose disconnect 
  mongoose.connect(MONGO_CONFIG.CONNECTION_STRING).then(() => console.log("Mongo connected")).catch(() => console.log("MongoDB error"));
  await connectToDB(sequelize);
});
