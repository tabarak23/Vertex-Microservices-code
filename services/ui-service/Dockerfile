FROM nginx:stable-alpine
# Remove default nginx config 
RUN rm /etc/nginx/conf.d/default.conf 
# Copy custom nginx config 
COPY nginx.conf /etc/nginx/conf.d/default.conf 
# Copy static files 
COPY index.html /usr/share/nginx/html/ 
COPY app.js /usr/share/nginx/html/ 
EXPOSE 80 
HEALTHCHECK --interval=30s --timeout=3s \ 
    CMD wget -qO- http://localhost || exit 1
