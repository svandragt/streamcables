init:
	uv sync

run:
	uv run python streamcables/streamcables.py

.PHONY: init run
