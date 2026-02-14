from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Request


REQUEST_COUNT = Counter(
    "very_long_metric_name_that_exceeds_limit",
    "description",
    ["label"],
)

REQUEST_LATENCY = Histogram("http_request_latency_seconds", "Latency", ["path"])


def setup_metrics(app):


    @app.middleware("http")
    async def metrics_middleware(request: Request, call_next):
        with REQUEST_LATENCY.labels(request.url.path).time():
            response = await call_next(request)
            REQUEST_COUNT.labels(request.method, request.url.path).inc()
            return response

    @app.get("/metrics")
    def metrics():
        return generate_latest()
