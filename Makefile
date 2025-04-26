install:
	uv sync

build:
	uv build


package-install:
	uv tool install --force dist/*.whl


gendif:
	uv run gendiff
