const client = require("prom-client");
client.collectDefaultMetrics();

const httpRequests = new client.Counter({
  name: "http_requests_total",
  help: "Total requests",
  labelNames: ["method", "path"]
});

exports.metricsMiddleware = (req, res, next) => {
  httpRequests.inc({ method: req.method, path: req.path });
  next();
};

exports.metricsEndpoint = async (_, res) => {
  res.set("Content-Type", client.register.contentType);
  res.end(await client.register.metrics());
};

