#!/usr/bin/env sh
#
# Makefile for SublimeConfluence plugin 
# 
# @author <bprinty@gmail.com>
# ------------------------------------------------


# config
# ------
VERSION := $$(python -c "`grep '__version__' ExecutionMode.py`; print __version__")


# targets
# -------
all:
    @echo "usage: make [release]"


release:
	TAG=${VERSION} && git tag -d $$TAG || echo "local tag available"
	TAG=${VERSION} && git tag $$TAG
	TAG=${VERSION} && git push origin :$$TAG || echo "remote tag available"
	TAG=${VERSION} && git push origin $$TAG

lint:
	flake8 ExecutionMode.py
