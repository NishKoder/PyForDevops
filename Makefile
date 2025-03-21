install:
	#install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
post_install:
	#post_install
	python -m textblob.download_corpora
format:
	#format code
	black *.py mylib/*.py
lint:
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	pip install httpx
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run container
	docker run -p 127.0.0.1:8081:8081 deploy-fastapi
deploy:
	#deploy
all: install post_install lint test deploy