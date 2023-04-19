
all: install exe

exe:
	python3 -B ./src/main.py

install:
	python3 -m pip install opencv-python
	python3 -m pip install matplotlib
	python3 -m pip install numpy
