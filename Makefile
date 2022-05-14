.DEFAULT_GOAL := install

install:
	python -m pip install -r requirements.txt
	python -m spacy download en

run:
	python main.py