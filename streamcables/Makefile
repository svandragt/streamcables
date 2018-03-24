WORKDIR = /vagrant/streamcables

serve:
	@echo "--> running server"
	pipenv run python streamcables.py

install:
	@echo "--> installing dependencies"
	pipenv install

update:
	@echo "--> updating dependencies"
	pipenv update
	pipenv lock -r > requirements.txt
