const express = require("express");
const productRoutes = require("./routes/product.routes");
const { metricsMiddleware, metricsEndpoint } = require("./metrics");

const app = express();

app.use(express.json());
app.use(metricsMiddleware);

app.use("/api/v1/products", productRoutes);
app.get("/metrics", metricsEndpoint);

/* 🔥 ADD THIS */
app.use((err, req, res, next) => {
  console.error("❌ ERROR:", err);
  res.status(500).json({ error: "Internal Server Error" });
});

module.exports = app;

