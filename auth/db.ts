import { Sequelize } from "sequelize";
import { DB_CONFIG } from "./config/db.config";


async function connectToDB(connector: Sequelize) {
  try {
    await connector.authenticate();
    console.log('Connection to Mysql has been established successfully.');
  } catch (error) {
    console.error('Unable to connect to the database:', error);
  }
}

const sequelize = new Sequelize(DB_CONFIG.CONNECTION_STRING)

export {
  sequelize,
  connectToDB
}