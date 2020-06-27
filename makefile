all: test

src := $(wildcard nperf/*.py)

test:
	python3 -m doctest nperf/shell.py
	python3 -m doctest nperf/web.py

dist: $(src)
	python3 setup.py sdist bdist_wheel

upload: dist
	python3 -m twine upload dist/*

clean:
	rm -rf nperf/__pycache__ build dist nperf.egg-info
