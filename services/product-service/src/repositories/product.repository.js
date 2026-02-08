const db = require("../db");

exports.create = async ({ name, price, stock }) => {
  const [result] = await db.query(
    "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
    [name, price, stock]
  );
  return { id: result.insertId, name, price, stock };
};

exports.getById = async (id) => {
  const [rows] = await db.query("SELECT * FROM products WHERE id=?", [id]);
  return rows[0];
};

exports.list = async () => {
  const [rows] = await db.query("SELECT * FROM products");
  return rows;
};

exports.updateStock = async (id, quantity) => {
  await db.query("UPDATE products SET stock=? WHERE id=?", [quantity, id]);
};

