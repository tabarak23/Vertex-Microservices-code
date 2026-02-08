const router = require("express").Router();
const service = require("../services/product.service");

router.post("/", service.create);
router.get("/:id", service.getById);
router.get("/", service.list);
router.patch("/:id/stock", service.updateStock);

module.exports = router;

