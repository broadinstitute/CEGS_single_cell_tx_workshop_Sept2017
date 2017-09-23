#!/bin/sh

set -ev

VERSION=`cat VERSION.txt`

docker build -t trinityctat/scellcegs2017:$VERSION .
docker build -t trinityctat/scellcegs2017:latest .

