all: test

test:
	python3 -m doctest nperf/shell.py
	python3 -m doctest nperf/web.py

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf nperf/__pycache__
