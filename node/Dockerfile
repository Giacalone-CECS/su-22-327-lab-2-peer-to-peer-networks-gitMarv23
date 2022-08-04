# pulling latest alpine from docker hub to build image
# small and a full linux distro
FROM alpine:latest

# copy files from current working directory into destination directory in the container
COPY . /app

# ensure packages are up to date via "cache busting"
# yes to install python package
RUN apk update && apk upgrade && apk add python3 

# set work directory to copied application directory
WORKDIR /app

# run a shell on launch
CMD ["sh", "-c", "python3", "./test.py"]