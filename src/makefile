IDIR =./include
CC=g++
CFLAGS=-I$(IDIR) -DDEBUG -pthread --std=c++11

ODIR=../obj

LIBS=-lm


dynamic_example: ../examples/dynamic_example.cpp
	g++ -o ../bin/dynamic_example ../examples/dynamic_example.cpp $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o