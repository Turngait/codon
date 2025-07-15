const express = require('express');
import mongoose from 'mongoose';
import 'dotenv/config'

import SignUpRouter from './routers/signup';
import SignInRouter from './routers/signin';
import GetUserInfo from './routers/getuserinfo';
import { APP_CONFIG } from './config/app.config';
import { MONGO_CONFIG } from './config/mongo.config';


const app = express();

app.use(express.json({
  inflate: true,
  strict: true,
  type: 'application/json'
}));


app.use('/signup', SignUpRouter)
app.use('/signin', SignInRouter)
app.use('/getinfo', GetUserInfo)

app.listen(APP_CONFIG.PORT, () => {
  console.log(`Server is running at https://localhost:${APP_CONFIG.PORT}`);
  // Add event for mongoose disconnect 
  mongoose.connect(MONGO_CONFIG.CONNECTION_STRING).then(() => console.log("Mongo connected")).catch(() => console.log("MongoDB error"));
});
