env:
	python -m venv venv
	. venv/bin/activate

remove:
	pip uninstall pkgbase -y

install:	
	pip install pkgbase

install_dev: env
	pip install --upgrade pip
	pip install -e ".[interactive]"

test:
	python setup.py test

lint:
	python setup.py flake8	

run:
	python pkgbase/main.py	
