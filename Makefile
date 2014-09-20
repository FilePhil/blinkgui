SHELL := /bin/bash
cur-dir := $(shell pwd)
all: deb

deb: 
	@ python3 setup.py sdist_dsc -d out;
	@ for x in `ls -d out/blink*/`; do \
		cp ../blink-deploy/general/* $$x/debian/; \
		cd $$x; \
		debuild; \
		cd ${cur-dir}; \
		rm -r dist; \
		rm *.tar.gz; \
		cp out/*.deb .; \
		rm -rf out; \
	done
