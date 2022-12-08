clean-python:  ## Remove python compiled and temporal files
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '.pytest_cache' -exec rm -fr {} +
	@rm -rf build/
	@rm -rf dist/
	@rm -rf myhooks.egg-info/

build:
	@python -m hooks.ensure-env.main

.PHONY: clean-python build
