FROM python:3.11-alpine
WORKDIR /app
COPY . .

ARG DB_HOST
ARG DB_USER
ARG DB_PASS
ARG SECRET_KEY
ARG DEBUG
ARG USE_POSTGRES
ARG USE_SSL
ARG TEMPLATE_DEBUG
ARG EMAIL_HOST
ARG EMAIL_HOST_USER
ARG EMAIL_HOST_PASSWORD
ARG EMAIL_PORT
ARG FRONTEND_URL
ARG GITHUB_TOKEN

ENV DB_HOST=${DB_HOST}
ENV DB_USER=${DB_USER}
ENV DB_PASS=${DB_PASS}
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=${DEBUG}
ENV USE_POSTGRES=${USE_POSTGRES}
ENV USE_SSL=${USE_SSL}
ENV TEMPLATE_DEBUG=${TEMPLATE_DEBUG}
ENV EMAIL_HOST=${EMAIL_HOST}
ENV EMAIL_HOST_USER=${EMAIL_HOST_USER}
ENV EMAIL_HOST_PASSWORD=${EMAIL_HOST_PASSWORD}
ENV EMAIL_PORT=${EMAIL_PORT}
ENV FRONTEND_URL=${FRONTEND_URL}
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

RUN set -ex \
  && apk add --no-cache --virtual .build-deps \
  postgresql-dev \
  build-base \
  netcat-openbsd \
  libffi-dev \
  && python -m venv /env \
  && /env/bin/pip install --upgrade pip \
  && /env/bin/pip install --no-cache-dir gunicorn \
  && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
  && runDeps="$(scanelf --needed --nobanner --recursive /env \
  | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
  | sort -u \
  | xargs -r apk info --installed \
  | sort -u)" \
  && apk add --virtual rundeps $runDeps \
  && apk del .build-deps

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PORT=8000

EXPOSE 8000

RUN python3 manage.py collectstatic --no-input && \
  chmod +x entrypoint.sh && \
  sed -i 's/\r$//' /app/entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]