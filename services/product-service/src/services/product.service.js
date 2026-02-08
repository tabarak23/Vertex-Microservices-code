const repo = require("../repositories/product.repository");

exports.create = async (req, res) => {
  try {
    const product = await repo.create(req.body);
    res.status(201).json(product);
  } catch (err) {
    console.error("CREATE PRODUCT ERROR:", err);
    res.status(500).json({ error: err.message });
  }
};

exports.getById = async (req, res) => {
  try {
    const product = await repo.getById(req.params.id);
    if (!product) return res.sendStatus(404);
    res.json(product);
  } catch (err) {
    console.error("GET PRODUCT ERROR:", err);
    res.status(500).json({ error: err.message });
  }
};

exports.list = async (_, res) => {
  try {
    const products = await repo.list();
    res.json(products);
  } catch (err) {
    console.error("LIST PRODUCTS ERROR:", err);
    res.status(500).json({ error: err.message });
  }
};

exports.updateStock = async (req, res) => {
  try {
    await repo.updateStock(req.params.id, req.body.quantity);
    res.sendStatus(204);
  } catch (err) {
    console.error("UPDATE STOCK ERROR:", err);
    res.status(500).json({ error: err.message });
  }
};

