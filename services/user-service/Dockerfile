#build image
FROM python:3.10-slim AS base





WORKDIR /build


# install build deps only if needed

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*







# Create virtualenv
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# copy dependency file first cacging
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


#runtime image
FROM python:3.10-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/*


# Create non-root user
RUN useradd -m -u 10001 appuser

WORKDIR /runtime

# Copy virtualenv from builder
COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set python env
#logs are printed immediately without delay which is good for docker logs
ENV PYTHONUNBUFFERED=1
# stops python from writing .pyc files which are not needed in prod 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/runtime

# Copy application code
COPY app ./app


# Install curl only for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# permissions
RUN chown -R appuser:appuser /runtime /opt/venv
USER appuser

EXPOSE 8001

# healtcheck this is only for local testing ,in prod im using Kubernetes liveness and readiness
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -f http://localhost:8001/health || exit 1

# Run with production ready settings
CMD ["uvicorn", "app.main:app", \
     "--host", "0.0.0.0", \
     "--port", "8001"]





