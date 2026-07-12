FROM python:3.14.6-slim-trixie

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.7 /uv /uvx /usr/local/bin/

RUN apt-get update \
    && apt-get install -y --no-install-recommends  build-essential curl libpq-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean \
    && useradd --create-home python \
    && chown python:python -R /app \
    && mkdir /static \ 
    && chown python:python -R /static

# USER python

# COPY --chown=python:python . .

COPY . .

ARG DEBUG="false"

ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="/app" \
    PATH="${PATH}:/home/python.local/bin" \
    USER="python" \
    BLOG_STATIC_ROOT="/static/" \
    BLOG_STATIC_URL="/static/" \
    BLOG_DEBUG="${DEBUG}" \
    BLOG_ALLOWED_HOSTS='["*"]' \
    BLOG_DATABASES__default__ENGINE="django.db.backends.postgresql" \
    BLOG_DATABASES__default__NAME="blog" \
    BLOG_DATABASES__default__USER="blog" \
    BLOG_DATABASES__default__HOST="blog_postgres" \
    DJANGO_SETTINGS_MODULE="django_blog.settings" \
    UV_SYSTEM_PYTHON=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

RUN uv sync --frozen --no-install-project --no-dev

RUN if [ "${DEBUG}" = "false" ]; then \
    SECRET_KEY=dummyvalue uv run python manage.py collectstatic --noinput; \
    fi

ENTRYPOINT ["/app/docker/entrypoint.sh"]

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "-c", "python:django_blog.gunicorn", "django_blog.wsgi"]