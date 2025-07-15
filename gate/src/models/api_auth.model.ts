import mongoose from 'mongoose';
const { Schema } = mongoose;

const apiAuthSchema = new Schema({
  contactEmail: String,
  clientName: String,
  authToken: String || null,
  apiToken: String || null,
  createdAt: Date,
  activeTill: Date,
});
const ApiAuth = mongoose.model('apiAuth', apiAuthSchema);
export default ApiAuth;
