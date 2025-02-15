FROM node:16-alpine as build-stage
WORKDIR /app

ARG VUE_APP_DOMAIN
ARG VUE_APP_DOMAIN_FRONTEND
ARG VUE_APP_DOMAIN_WEBSOCKET
ARG VUE_APP_DOMAIN_WEBSOCKET_PORT

ENV VUE_APP_DOMAIN=${VUE_APP_DOMAIN}
ENV VUE_APP_DOMAIN_FRONTEND=${VUE_APP_DOMAIN_FRONTEND}
ENV VUE_APP_DOMAIN_WEBSOCKET=${VUE_APP_DOMAIN_WEBSOCKET}
ENV VUE_APP_DOMAIN_WEBSOCKET_PORT=${VUE_APP_DOMAIN_WEBSOCKET_PORT}

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY --from=build-stage /app/entrypoint.sh /entrypoint.sh
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN chmod +x /entrypoint.sh

EXPOSE 80
CMD ["/entrypoint.sh","nginx", "-g", "daemon off;"]
