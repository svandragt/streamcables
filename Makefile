build:
	rm -rf dist && pipenv run pyinstaller streamcables/streamcables.py -n streamcables --onefile

init:
	pipenv install --dev

pack:
	pipenv run python setup.py sdist

run:
	pipenv run python streamcables/streamcables.py

.PHONY: build init pack run
