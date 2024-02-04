#!/bin/bash

# 
sudo docker-compose pull 

DOCKER_BUILDKIT=1

# Build a Docker
sudo docker-compose build

# Run a Docker
sudo docker-compose up

