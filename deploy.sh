#!/bin/bash

#yellow light
ansible-playbook deploy.yml -e "project=$project"
ret=$?
if [ $ret -ne 0 ]; then
    #red light
else 
    #green light
fi

#repeat
