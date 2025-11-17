
# KG Build Notebook Template

A minimal notebook-driven starter to import web pages into a WordLift knowledge graph using the WordLift Python SDK. The `kg_import.ipynb` notebook wires up a configuration file and a custom callback so you can adapt the import to your project.

## Prerequisites
- Python 3.11 or 3.12
- [`uv`](https://docs.astral.sh/uv) for dependency and environment management
- access to a WordLift workspace (set the credentials in your environment or `.env` file before running the notebook)

## Quick start
1) Install `uv` if you do not have it:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
2) Create the virtual environment and install dependencies:
   ```bash
   uv sync
   ```
   Add `--all-extras` if you also want the dev tools (`ruff`, `pre-commit`, `pytest`, `nbstripout`).
3) Activate the environment (optional) or prefix commands with `uv run`:
   ```bash
   source .venv/bin/activate
   ```
4) Set any required environment variables in a `.env` file at the repo root (the SDK will read them via `python-dotenv`). This is typically where you place API credentials and workspace settings.
5) Start the notebook:
   ```bash
   uv run jupyter notebook kg_import.ipynb
   ```
6) Open `kg_import.ipynb` in your browser and run the cells top-to-bottom. The first cell ensures required packages are present; the second loads your configuration and kicks off the import workflow.

## Configure the import
- Edit `config/default.py` to point to your sitemap, page types, concurrency, and import strategy.
- Customize the callback in `app/overrides/web_page_import_protocol.py` to handle the `WebPageImportResponse` objects (e.g., logging, persistence, or additional processing).
- Add templates or additional assets under `data/` as needed.

## Tooling
- Install Git hooks after syncing deps: `uv run pre-commit install`
- Format/lint: `uv run ruff check .`
- Tests (if/when added): `uv run pytest`

## Troubleshooting
- If the notebook fails to authenticate, double-check the credentials in your `.env`.
- Re-run `uv sync` after updating dependencies in `pyproject.toml`.
