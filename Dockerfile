FROM phusion/baseimage:bionic-1.0.0

# Use baseimage-docker's init system:
CMD ["/sbin/my_init"]

# Install dependencies:
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    sudo \
    wget \
    git \
    make \
    busybox \
    build-essential \
    nodejs \
    imagemagick \
    ffmpeg \
    unzip \
    python3-pip \
    python3 \
    inotify-tools \

 && mkdir -p /home/stuff
# Set work dir:
RUN chmod +x awesomeshot

# Copy files:
RUN cp awesomeshot $PREFIX/bin
RUN pip3
CMD bash /home/startbot.sh
