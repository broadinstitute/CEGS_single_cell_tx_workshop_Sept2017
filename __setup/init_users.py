#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os, sys, re
import logging
import argparse
import subprocess

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)


docker_image = "trinityctat/scellcegs2017"

rstudio_base_port = 9000

def main():

    parser = argparse.ArgumentParser(description="instantiate user spaces", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--num_users", type=int, default="", required=True, help="number of users")
    parser.add_argument("--ip_addr", type=str, required=True, help="IP address for server")

    #parser.add_argument("--user_id_start", type=int, default=1, help="index to start user IDs (ex. 1)")
    
    #parser.add_argument("--apache_base_port", type=int, default=8001, help="base port for apache")
    #parser.add_argument("--gateone_base_port", type=int, default=9001, help="base port for gateone")
    #parser.add_argument("--ssh_base_port", type=int, default=10001, help="base port for rstudio")

    args = parser.parse_args()

    for i in range(0, args.num_users):
        
        user_rstudio_port = rstudio_base_port + i
        
        # launch docker
        cmd = str("docker run " +
                  " -p {}:8787 ".format(user_rstudio_port) +
                  " --name scell_{} -d {}".format(user_rstudio_port, docker_image))
        
        #subprocess.check_output(cmd)
        
        print(cmd)
        
    sys.exit(0)
 
####################
 
if __name__ == "__main__":
    main()
