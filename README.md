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
### Docker File for Redis SErver:
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

## Run the application Container

## Communication between Containers

## Docker Compose
