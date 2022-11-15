#!/bin/sh
APP_HOME=/home/ec2-user/deploy/ProjectTR-api

function stop(){
	echo 'stop...'
	
	PID=$(ps -ef | grep serverApplication.py | grep -v "grep" | awk '{print $2}')
  echo "- pid : ${PID}"
    
	if [[ ! -z $PID ]]; then
		echo "- kill process"
		kill -15 ${PID}
	else
		echo "- no process"
	fi                  
}

function start(){
	echo 'start ...'
	python3 ${APP_HOME}/serverApplication.py &
}

function restart(){
	echo 'restart ...'
	stop
	start
}

OPTION=$1

case $OPTION in
                "start")
                start
                ;;

                "stop")
                stop
                ;;
                
                "restart")
                restart
                ;;

        *)
            echo "[usage] : $0 start|stop|restart"
        ;;
esac
