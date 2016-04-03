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
    @echo "usage: make [test|release]"


.PHONY: test
test:
	@echo "No tests yet ..."


release: test
	TAG=${VERSION} && git tag -d $$TAG || echo "local tag available"
	TAG=${VERSION} && git push origin :$$TAG || echo "remote tag available"
	TAG=${VERSION} && git tag $(TAG) && git push origin $$TAG
