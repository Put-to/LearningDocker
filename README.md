# LearningDocker
This is a docker learning path. I may set it to public in the future.
For this, I'll mainly use a Python Django app.

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
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt   ##Run any command
COPY . .
EXPOSE $PORT  ##Port that can be accessed from outside.
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
To run the Docker image, make sure the Docker engine is running. Then use the run command.
```
docker run -d -p 8000:8000 python_server
```
-p 8000:8000 makes sure that the 8000 port inside the image is available on the 8000 port outside the image
To stop the Docker application use the stop command
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

Use the ps command to see all container Id, names, and ports
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

Pull and run Redis container:
```
docker pull redis:latest
```
```
docker run -p 6379:6379 -d redis
```

## Volumes

A Volume mount protects the data from being lost if the container fails.
```
docker run -p <ports> -v <directory> <image>
```

as

```
docker run -d -p 8000:8000 -v${pwd}/db:/app/db python_server
```


## Communication between Containers

### Bridge Network
Creates a bridge that helps containers to talk to each other. Only the containers connected via bridges will be able to talk to each other.

### Create a Bridge:
```
docker network create --driver bridge <Network_Name>
```
See all networks:
```
docker network ls
```
Remove a network:
```
docker network rm <network>
```

### Add a container to the bridge when running:
```
docker run -d --net=<Network_name> --name<Container_name> <Custom_Container_name>
```



## Docker Compose
- Uses YAML config Files
- Build one or more images
- Start and Stop services
- Stream the log output of running services

### Indentation matters with YAML files

### Sample Docker-compose file:
```
version: '3.8'

services:
  django:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/0

  redis:
    image: redis:latest
    ports:
      - "6379:6379"

  celery:
    build: .
    command: celery -A ImageGen worker -l info -P eventlet
    volumes:
      - .:/app
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/0
  

```


### Build a docker-compose file
```
docker-compose build
```

### Run services
```
docker-compose up
```

### Shut down and delete a container
```
docker-compose down
```

# Extra Stuff 
- The entire app lifecycle can be managed using docker compose.
- Log all services.

## YAML
- Uses Maps and Lists
- Indentation matters
-  Maps:
- - name: Value Pairs
   - Maps can contain other maps for more complex data structures.
- Lists:
- - Sequences of Items
  - Multiple maps can be defined in a list.

