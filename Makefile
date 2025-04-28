install:
	uv sync

build:
	uv build


package-install:
	uv tool install --force dist/*.whl


lint:
	uv run ruff check --fix gendiff


gendif:
	uv run gendiff

diff:
	uv run diff_script.py filepath1.json filepath2.json
