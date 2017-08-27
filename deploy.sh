#!/bin/bash

project="project-web1"

#yellow light

ansible-playbook deployer.yml -e "project=$project" &>/tmp/ansiblexecution.log
ret=$?
if [ $ret -ne 0 ]; then
    #red light
	exit $ret
else 
    #green light
	exit $ret
fi

#repeat
