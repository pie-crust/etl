#!/bin/bash
trap '' SIGINT
trap ''  SIGQUIT
trap '' SIGTSTP

pause(){
	local m="$@"
	echo "$m"
	read -p "Press [Enter] key to continue..." key
}

while :
do
	# show menu
	clear
	echo "---------------------------------"
	echo "	     M A I N - M E N U"
	echo "---------------------------------"
	echo "1. Pause"
	echo "2. Start GTX"
	echo "3. Start GRDS"
	echo "4. Start GFIN"
	echo "5. Exit"
	echo "---------------------------------"
	read -r -p "Enter your choice [1-5] : " c
	# take action
	case $c in
		1) pause "$(date)";;
		2) time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx
		3) time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx
		4) time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx

		5) break;;
		*) Pause "Select between 1 to 5 only"
	esac
done


while true
do
	echo "Press CTRL+C to stop cli.py "
	time python3 cli.py  -nopp 1 -dcf config/db_config.DEV.json -pcf config/proc/g3/dir_gtx_vertica/gtx.json --proc_params  ./legacy/gtx
	if (disaster-condition)
	then
		break
	fi

	sleep 60
done