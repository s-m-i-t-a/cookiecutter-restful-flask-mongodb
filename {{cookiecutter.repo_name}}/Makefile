.PHONY: clean-pyc clean-build docs clean requirements client

SHELL = bash
OS := $(shell uname)

PROJECT := {{ cookiecutter.repo_name }}
LOCALPATH := $(CURDIR)
PYTHONPATH := $(PYTHONPATH):$(LOCALPATH)/$(PROJECT)
MANAGE := $(PROJECT)/manage.py
HEROKU_RUN := heroku run

-include recipes/config
-include recipes/.config

PYTHON := $(shell which python)
PIP := $(shell which pip)
VENV := $(shell which pyvenv)


help:
	@echo "clean - vycisti projekt od docasnych souboru"
	@echo "coverage - spusti test a vypise pokryti testy"
	@echo "coverage-report - vytvori html report z prikazu 'coverage'"
	@echo "create-env - vytvori virtualni prostredi pro python"
	@echo "docs - vytvori dokumentaci projektu"
	@echo "install - nainstaluje systemove zavislosti (napr. MongoDB)"
	@echo "requirements - nainstaluje zavislosti pro projekt"
	@echo "startdb - nastartuije databazovy stroj"
	@echo "stopdb - zastavi databazovy stroj"
	@echo "tags - vytvori soubory TAGS, tags, ID pro snadnou navigaci ve zdrojovych kodech (jen pro vim, emacs)"
	@echo "test - spusti testy"


include recipes/Makefile.$(OS)


requirements:
	$(PIP) install -r $(REQUREMENTS)


install: dependencies create-env


create-env:
	$(VENV) $(VIRTUALENVS_DIR)$(PROJECT)


clean: clean-build clean-docs clean-pyc clean-test clean-tags

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-db:
	mongo $(DB) --eval "db.dropDatabase()"

clean-docs:
	rm -rf $(DOCS_DIR)/_build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

clean-tags:
	rm -f tags
	rm -f TAGS
	rm -f ID

docs: clean-docs
	$(MAKE) -C $(DOCS_DIR) html

tags: clean
	build_tags -i -v

test: clean
	tox --skip-missing-interpreters

coverage:
	py.test --cov

coverage-report:
	py.test --cov --cov-report=html
	open htmlcov/index.html
