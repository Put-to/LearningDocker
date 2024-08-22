# LearningDocker
This is a docker learning path. I may set it to public in the future.
For this, I'll mainly use a Python Django app and a ReactJs app.

### Why Docker?
- Run apps anywhere
- Easy to Automate
- Version Safety/Environment Consistency - Makes sure the project is always running in the same Environment.

## Environment Setup
Install Docker Desktop on Windows/Mac
Install Docker Engine on Linux

Test whether docker is properly installed by running a default container:
```
docker run -d -p 80:80 docker/getting-started
```
Now Run:
```
docker ps -a
```
to check the running container.
Visit localhost to verify the running app

Stop and remove the docker container with the following commands:
```
docker stop CONTAINER_ID
docker rm CONTAINER_ID
```


## Creating an Application Image
Docker File --> Docker Build --> Docker Image
### Docker File for Redis Server:
```
FROM python:3.11-slim   ##Docker Image for Redis
LABEL author="Tanishq"   ##Basic label
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt   ##Run any command
COPY . .
EXPOSE $PORT  ##Port that can be used to access from outside.
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"] ##Run the server
```
### Create a .dockerignore file and add files you don't want to copy.

## Building the Docker Image
Run the build command in the terminal where your dockerfile is located.
'.' after the command specifies where the dockerfile is located.
```
docker build -t python_server .

```
If your dockerfile is named something other than .dockerfile, use -f to select it
```
docker build -t python_server -f python.dockerfile .
```

## Run the application Container
To run the Docker image, make sure the docker engine is running. Then use the run command.
```
docker run -d -p 8000:8000 python_server
```
-p 8000:8000 makes sure that the 8000 port inside the image is available on 8000 port outside the image
To stop the Docker application use stop command
```
docker stop <container_id>
```

Remove the Container using the rm command
```
docker rm <container_id>
```

Remove the docker image using the rmi command
```
docker rmi python_server
```

Use the ps command to see all container Id, names and ports
```
docker ps
```

Use logs to view the log of the image
```
docker logs <container_id_or_name>
```

## Deploy this image to register
Build an image with your username
```
docker build -t <username>/<imagename>:<tag> -f <Dockerfile> .
```
as
```
docker build -t putato/python_server:1.0 -f python.dockerfile .
```

login to docker
```
docker login
```
Now use the push command to push to Docker Hub by default
```
docker push <Image>
```
as
```
docker push putato/python_server:1.0
```

## Communication between Containers

## Docker Compose
