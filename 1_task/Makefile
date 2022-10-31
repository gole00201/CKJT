CC=gcc
FLAGS=-fPIC -Wall -shared -o 
all:
	$(CC) $(FLAGS) libstruct.so struct.c
	python3 build.py
	python3 main.py
