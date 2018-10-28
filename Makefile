init:
	pipenv install

run:
	cd streamcables; pipenv run ./streamcables.py

.PHONY: init run