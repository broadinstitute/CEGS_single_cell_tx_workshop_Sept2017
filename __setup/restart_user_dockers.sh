#!/bin/bash

docker ps -a | grep 'scell_' | awk '{ print $1 }' | xargs -n1 docker restart


