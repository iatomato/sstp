#!/bin/bash

declare install_dir=src/service.py
sudo chomd a+x $install_dir && sudo cp $install_dir /usr/sbin/v2ctl

if [ $? -eq 0 ]
then
	echo "install [OK]"
	echo "Typing v2ctl on console (terminal)"
fi
