#!/bin/sh

clear
mode=$1
echo "Mode chosen: $mode"

if [ "$mode" = "build" ]; then
	docker-compose -f docker-compose.yml -f docker-compose.development.yml build
else
	if [ "$mode" = "up" ]; then
		docker-compose -f docker-compose.yml -f docker-compose.development.yml up --force-recreate
	else
		if [ "$mode" = "jupyter" ]; then 
			docker-compose -f docker-compose.yml -f docker-compose.development.yml run --rm -p 8888:8888 web python manage.py shell_plus --notebook
		else
			echo "please enter a valid mode"
		fi
	fi
fi 
