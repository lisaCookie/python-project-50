install:
	uv sync

	uv build

	uv tool install --force dist/*.whl


lint:
	uv run ruff check --fix gendiff


test-coverage:

	uv run pytest --cov


check:
	uv run pytest


