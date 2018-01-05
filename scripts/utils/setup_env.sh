#!/bin/bash

# Clean any artifacts
echo "--> Cleaning artifacts"
cd /srv/funny/pycon2018 && make clean


# Make sure that the docker container can write to these directories
echo "--> Updating permissions for docker access"
find /srv/funny/pycon2018 -iname "migrations" -type "d" | xargs sudo chmod 777
sudo chmod 777 /srv/funny/pycon2018/run
sudo chmod 777 /srv/funny/pycon2018/logs
sudo chmod 777 /srv/funny/pycon2018/logs/*.log
sudo chmod 777 /srv/funny/pycon2018/pyconph/static
sudo chmod 777 /srv/funny/pycon2018/pyconph/media

# Apply migrations
echo "--> Applying migrations"
cd /srv/funny/pycon2018
source scripts/utils/django_manage.sh migrate
