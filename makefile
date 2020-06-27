all: test

test:
	python3 -m doctest nperf/shell.py

clean:
	rm -rf nperf/__pycache__
