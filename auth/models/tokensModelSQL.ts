const { Sequelize } = require('sequelize');
import { sequelize } from "../db";

const Tokens = sequelize.define("tokens", {
  id: {
    type: Sequelize.INTEGER,
    autoIncrement: true,
    primaryKey: true,
    allowNull: false
  },
  user_id: {
    type: Sequelize.INTEGER,
    allowNull: false
  },
  token: {
    type: Sequelize.STRING,
    allowNull: false
  },
  active_til: {
    type: Sequelize.DATE,
    allowNull: false
  },
  createdAt: {
    type: Sequelize.DATE,
    allowNull: false
  }
});

sequelize.sync().then(result=>console.log("Tokens created"))
.catch(err=> console.log(err));

export default Tokens;