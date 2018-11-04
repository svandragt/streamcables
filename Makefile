init:
	pipenv install --dev

run:
	pipenv run python streamcables/streamcables.py

.PHONY: init run
