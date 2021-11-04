setup:
	python3 -m venv menv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


lint:
	pylint --disable=R,C main.py

all: install lint test