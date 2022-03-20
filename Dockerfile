FROM ubuntu:latest

# Use baseimage-docker's init system:

# Install dependencies:
RUN apt-get update && apt-get install python3-pip python3 inotify-tools imagemagick -y

# Set work dir:
RUN mkdir /app
RUN chmod 777 /app
WORKDIR /app
ADD . /app
RUN chmod +x awesomeshot

# Copy files:
RUN cp awesomeshot $PREFIX/bin
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
