#!/bin/sh

set -ev

VERSION=`cat VERSION.txt`

docker push trinityctat/scellcegs2017:${VERSION}
docker push trinityctat/scellcegs2017:latest
