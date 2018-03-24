WORKDIR = /vagrant/streamcables

serve:
	@echo "--> running server"
	cd $(WORKDIR);pipenv run python streamcables.py

install:
	@echo "--> installing dependencies"
	cd $(WORKDIR);pipenv install

update:
	@echo "--> updating dependencies"
	cd $(WORKDIR);pipenv update; pipenv lock -r > requirements.txt
