#!/bin/sh

python postgres-wait.py
flask db upgrade
if [ $? ]; then
  flask run
fi
