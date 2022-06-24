.DEFAULT_GOAL := install

install:
	python -m pip install -r requirements.txt
	python -m spacy download en

run:
	streamlit run main.py