#!/bin/bash

project=$1

#yellow light
echo "VAMOS A VÉ"

ansible-playbook deployer.yml -e "project=$project" &>/tmp/ansiblexecution.log
ret=$?
if [ $ret -ne 0 ]; then
    #red light
	echo "ERROR, FUSIÓN EN EL NÚCLEO"
else 
    #green light
	echo "FLAMA, COMPADRE"
fi

#repeat
