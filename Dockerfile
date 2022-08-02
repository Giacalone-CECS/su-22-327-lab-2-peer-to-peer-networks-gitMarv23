# pulling latest alpine from docker hub to build image
# small and a full linux distro
FROM alpine:latest

# copy files from current working directory into destination directory in the container
COPY . /app

# ensure packages are up to date via "cache busting"
RUN apk update && apk upgrade

#yes to install python package
RUN apk add python3

# change work directory to app directory inside container
WORKDIR /app