#!/bin/bash

echo "Installing and setting up supervisord"
source /srv/funny/pycon2018/scripts/supervisord/setup_supervisord.sh

source /srv/funny/pycon2018/scripts/utils/setup_env.sh

cd /srv/funny/pycon2018 && make deploy

echo "--> [default] Starting ssh service"
/usr/sbin/sshd -D
