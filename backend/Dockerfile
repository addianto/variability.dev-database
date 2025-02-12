FROM python:3.11-alpine
WORKDIR /app
COPY . .
# COPY ./ddueruemweb/.env.production /app/ddueruemweb/.env
COPY ./ddueruemweb/.env ./ddueruemweb/.env
COPY . .

SHELL ["/bin/sh", "-o", "pipefail", "-c"]
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

RUN python3 ./manage.py collectstatic --no-input && chmod +x /app/entrypoint.sh
CMD ["sh", "/app/entrypoint.sh", "ls"]