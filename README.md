# LearningDocker
This is a docker learning path. Maybe I will set it to public in the future.
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

## Run the application Container

## Communication between Containers

## Docker Compose
