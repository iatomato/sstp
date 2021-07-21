#!/bin/bash

declare install_dir=src/service.py
sudo chomd a+x $install_dir && sudo cp $install_dir /usr/sbin/v2ctl

if [ $? -eq 0 ]
then
	echo "Installation >>> [OK]"
	echo "Try typing ssv2"
fi
