coverage-all:
		coverage erase
		coverage run --source admiralty-tides -m unittest
		coverage xml

coverage: coverage-all
		coverage report --show-missing

test:
	    pytest --junitxml=test-reports/junit.xml
	
lint:
	    flake8 .

acceptance-test:
	    behave acceptance-tests/

sonar:
		sonar-scanner \
				  -Dsonar.projectKey=ngfgrant_admiralty-tides \
				  -Dsonar.organization=ngfgrant-github \
				  -Dsonar.sources=. \
				  -Dsonar.host.url=https://sonarcloud.io \
				  -Dsonar.login=${sonar_login}

dist: clean
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	twine check dist/*
	ls -l dist

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -f .coverage.xml
	rm -f test-results/
