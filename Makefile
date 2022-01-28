.PHONY: help clean dev docs package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "  docs	create pydocs for all relveant modules"
	@echo "	 test	run all tests with coverage"

clean:
	rm -rf dist/*

dev:
	pip install -r requirements-dev.txt
	pip install pytest pytest-cov flake8
	pip install -e .

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	flake8 confite  --ignore F401,F403
	pytest -v --junitxml=test_report.xml --cov-report xml --cov  confite
	coverage report -m
	coverage xml -i
	coverage html


