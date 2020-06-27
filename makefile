all: test

test:
	python3 -m doctest nperf/shell.py
