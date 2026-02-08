const mysql = require("mysql2/promise");

function required(name) {
  if (!process.env[name]) {
    throw new Error(`❌ Missing required env var: ${name}`);
  }
  return process.env[name];
}

const pool = mysql.createPool({
  host: required("PRODUCT_DB_HOST"),
  user: required("PRODUCT_DB_USER"),
  password: required("PRODUCT_DB_PASSWORD"),
  database: required("PRODUCT_DB_NAME"),
  port: process.env.PRODUCT_DB_PORT || 3306,
  waitForConnections: true,
  connectionLimit: Number(process.env.DB_POOL_SIZE || 10),
});

module.exports = pool;

