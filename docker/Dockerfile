FROM rocker/rstudio
MAINTAINER Brian Haas (bhaas@broadinstitute.org)

######################
## Environment
######################

### locations
ENV BIN /usr/local/bin
ENV DATA /usr/local/data
ENV SRC /usr/local/src

### User setup
RUN groupadd -g 2000 training && useradd -m -u 2000 -g 2000 training
RUN echo 'training:training' | chpasswd
RUN chsh -s /bin/bash training
ENV HOME=/home/training
RUN echo "alias ll='ls -la -G'" >> /home/training/.profile
RUN usermod -G training,www-data training

# ports
EXPOSE 8787

RUN apt-get update && \
    apt-get install -y unzip wget git \
    r-base r-base-dev \
    libssl-dev libcurl4-openssl-dev libxml2-dev libxt-dev libgstreamer0.10-0 ibgstreamer-plugins-base0.10-0 \
    libcairo2-dev default-jre htop


RUN chmod 777 /usr/local/lib/R/site-library

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");library(BiocInstaller); biocLite("tidyverse", dep = TRUE')
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");library(BiocInstaller); biocLite("vioplot", dep = TRUE)'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");library(BiocInstaller); biocLite("devtools", dep = TRUE)'



