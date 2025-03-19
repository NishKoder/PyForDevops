install:
	#install command
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	#flack8 or #pylint
test:
	#test
deploy:
	#deploy
all: install lint test deploy