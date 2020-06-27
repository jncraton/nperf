all: test

test:
	python3 -m doctest nperf/shell.py
	python3 -m doctest nperf/web.py

clean:
	rm -rf nperf/__pycache__
