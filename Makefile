install:
	uv sync

build:
	uv build


package-install:
	uv tool install --force dist/*.whl


lint:
	uv run ruff check --fix gendiff


test-coverage:

	uv run pytest --cov


check:
	uv run pytest


