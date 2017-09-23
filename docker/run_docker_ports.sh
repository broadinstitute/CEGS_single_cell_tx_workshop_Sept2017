sudo docker run --rm -it -v `pwd`/../../:/data -p 9000:80 -p 9001:443 -p 9002:8787 trinityctat/scellcegs2017 $*
