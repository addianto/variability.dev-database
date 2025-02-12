FROM python:3.11-alpine
WORKDIR /app
COPY . .
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

COPY ./entrypoint.sh /app/entrypoint.sh
# COPY ./core/auth/.env /app/core/auth/.env
# COPY ./ddueruemweb/.env /app/ddueruemweb/.env
COPY ./manage.py /app/manage.py

RUN python3 ./manage.py collectstatic --no-input && chmod +x /app/entrypoint.sh && sed -i 's/\r$//' /app/entrypoint.sh && ls -la .
CMD ["sh", "/app/entrypoint.sh", "ls"]