# To be run from the main folder.

docker run --rm -it -v "$PWD/src":"/code/src" -v "$PWD/tests":"/code/tests" oop-patterns-in-python pytest ./tests/