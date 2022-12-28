# To be run from the main folder.

docker run --rm -it -v "$PWD":"/code/" oop-patterns-in-python pylint ./src/ ./tests/