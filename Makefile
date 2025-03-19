install:
	#install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib *.py
build:
	#build container
deploy:
	#deploy
all: install format lint test build deploy