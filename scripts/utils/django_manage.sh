#!/bin/bash

ACTION=$1
if [[ $ACTION == collectstatic* ]]; then
    sudo su - funny -c """
    cd /srv/funny/pycon2018
    python3 manage.py $ACTION --no-input
    """
else
    sudo su - funny -c """
    cd /srv/funny/pycon2018
    python3 manage.py $ACTION
    """
fi
