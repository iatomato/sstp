#!/bin/bash
DIR=src/v2rayT.py
sudo chomd a+x ${DIR} && mv ${DIR} /usr/sbin/v2rayT
if [ $? -eq 0 ]
then
	echo "done!"
	printf "Try enter \"v2rayT\" to use it"
fi
