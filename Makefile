init:
	pipenv install --dev

pack:
	pipenv run python setup.py sdist

run:
	pipenv run python streamcables/streamcables.py

.PHONY: init pack run
