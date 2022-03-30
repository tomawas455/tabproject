#!/bin/sh

flask_path=flask
if [ $1 ]; then
  flask_path=$1/flask
fi 

"$flask_path" db migrate
"$flask_path" db upgrade
