FROM ghcr.io/astral-sh/uv:0.6-python3.8-bookworm-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
  UV_LINK_MODE=copy

RUN apt update \
  && apt install -y --no-install-recommends graphviz build-essential \
  && rm -rf /var/lib/apt/lists/*

RUN --mount=type=cache,target=/root/.cache/uv \
  --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --frozen --no-install-project

RUN uv run --frozen --module nltk.downloader punkt stopwords

COPY data src config-example.toml config.toml pyproject.toml uv.lock ./

ENTRYPOINT ["uv", "run", "--frozen"]
