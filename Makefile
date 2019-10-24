SHELL := /bin/bash

create:
	python3 -m venv env

install:
	source env/bin/activate && pip3 install -r requirements.txt

ipython:
	source env/bin/activate && ipython --pdb

login:
	source env/bin/activate && python3 login.py
