
# Makefile for twinx_tick_utils

MODULE = twinx_tick_utils.py

install:
	pip install matplotlib numpy

test:
	python $(TEST)

lint:
	flake8 $(MODULE)

clean:
	rm -f *.pyc __pycache__/*

.PHONY: install test lint clean
