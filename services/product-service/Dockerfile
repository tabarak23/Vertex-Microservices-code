#build image
FROM node:18-alpine AS base

WORKDIR /build

COPY package.json package-lock.json ./

#production deps only
RUN npm ci 


#runtime image
FROM node:18-alpine

# create non root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /runtime

# copy node_modules
COPY --from=base /build/node_modules ./node_modules

# copy source
COPY src ./src

ENV PORT=8002

EXPOSE 8002

# healthcheckss this is only for local testing ,in prod im using Kubernetes liveness and readiness 
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost:8002/metrics || exit 1

# assign ownership
RUN chown -R appuser:appgroup /runtime
USER appuser

CMD ["node", "src/server.js"]
