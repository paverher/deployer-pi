#!/bin/bash

project="project-web1"

#yellow light
export ANSIBLE_CONFIG="/home/pablo.vera/Documents/tfg/ansible.cfg"
ansible-playbook /home/pablo.vera/Documents/tfg/deployer.yml -e "project=$project" &>/tmp/ansiblexecution.log
ret=$?
if [ $ret -ne 0 ]; then
    #red light
	exit $ret
else 
    #green light
	exit $ret
fi

#repeat
