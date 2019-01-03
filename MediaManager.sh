#!/bin/sh

cd `dirname $0`
CURRENT_DIR=`pwd`
command=$1

run(){
	# eval ”. mmvenv/bin/activate”
	eval ". mmvenv/bin/activate"
	eval "nohup python mm/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 < /dev/null &"
	echo "RUN"
}

stop(){
	pids=(`ps -ef | grep runserver | awk '{print $2;}'`)

	kill -9 ${pids[1]}

	echo "STOP"
}


if [ $command = "run" ]; then
	run
else
	stop
fi

