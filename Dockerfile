FROM ubuntu:latest

# Use baseimage-docker's init system:

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

# Set work dir:
WORKDIR /home
COPY * /home
RUN chmod +x awesomeshot

# Copy files:
RUN cp awesomeshot $PREFIX/bin
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
