SHELL := /bin/bash
cur-dir := $(shell pwd)

deb: 
	@ python3 setup.py --command-packages=stdeb.command sdist_dsc -d out;
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

ui:
	 pyside-rcc -py3 res/res.qrc -o res_rc.py
	 pyside-uic mainwindow.ui -o mainwindow.py
	 pyside-uic color_transition_dialog.ui -o color_transition_dialog.py
	 pyside-uic lg_dialog.ui -o lg_dialog.py
	 pyside-uic text_dialog.ui -o text_dialog.py
	 pyside-uic ethernet_dialog.ui -o ethernet_dialog.py
	 pyside-lupdate blinkGui.pro
