#build image
FROM maven:3.9.6-eclipse-temurin-17 AS base

WORKDIR /build

# cache deps first
COPY pom.xml .
RUN mvn -B dependency:go-offline

# copy source and build
COPY src ./src
RUN mvn -B clean package -DskipTests

#runtime image
FROM eclipse-temurin:17-jre-jammy

#install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

#create non root user
RUN useradd -m -u 10001 appuser

WORKDIR /app

#copy jar from builder
COPY --from=base /build/target/order-service-0.0.1-SNAPSHOT.jar app.jar


# expose port
EXPOSE 8003

# healthcheck this is only for local testing ,in prod im using Kubernetes liveness and readiness 
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8003/actuator/health || exit 1

# permissions
RUN chown -R appuser:appuser /app
USER appuser

# run app
ENTRYPOINT ["java", "-jar", "app.jar"]
