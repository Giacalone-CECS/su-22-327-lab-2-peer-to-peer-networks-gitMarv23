# pulling latest alpine from docker hub to build image
# small and a full linux distro
FROM alpine:latest

# copy files from current working directory into destination directory in the container
COPY . /home/lab2

#install ping 3
#RUN apk update &&apk upgrade && apk add ping

# ensure packages are up to date via "cache busting"
# yes to install python package
RUN apk update && apk upgrade && apk add python3 && apk add py3-pip && pip install ping3

# set work directory to copied application directory
WORKDIR /home/lab2