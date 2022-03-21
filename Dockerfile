FROM phusion/baseimage:bionic-1.0.0

# Use baseimage-docker's init system:
CMD ["/sbin/my_init"]
RUN apt-get update && apt-get install python3-pip python3 inotify-tools imagemagick -y

COPY awesomeshot /home
COPY main.py /home
COPY /plugins /home/stuff
COPY 

# Run config.sh and clean up APT:
RUN sh /home/config.sh \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy files:
RUN cp awesomeshot $PREFIX/bin
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
