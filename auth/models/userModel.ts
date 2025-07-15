import mongoose from 'mongoose';
const { Schema } = mongoose;

const userSchema = new Schema({ 
  email: String,
  pass: String,
  paper: String,
  ips: [String],
  token: String,
  createdAt: String
});
const User = mongoose.model('user', userSchema);
export default User;