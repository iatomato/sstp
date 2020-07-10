#!/bin/bash
DIR=src/v2rayT.py
sudo chomd a+x ${DIR} && mv ${DIR} /usr/sbin/v2rt
if [ $? -eq 0 ]
then
	echo "done!"
	printf "Try enter \"v2rt\" to use it\n"
fi
