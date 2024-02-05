# Web Tracking System
>Important Compatibility Note: This application and all associated deployment scripts are specifically tailored for the Ubuntu operating system and command environment. While Docker and Docker Compose facilitate some level of portability, the unique configurations and scripts provided here are optimized for Ubuntu and may not work as intended on other platforms.

## Project Overview
The Online Track System is designed to provide real-time tracking and status updates for various entities. This system is particularly useful for applications requiring constant monitoring and updates, such as logistics, asset management, and personal tracking.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Preinstallation](#preinstallation)
- [Installation](#installation)

## Features
- Real-time tracking of entities
- Status update functionality
- Interactive web interface for easy access and monitoring
- Scalable architecture to support a large number of trackable entities

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose installed on your machine
- Python 3.12 or higher

## Preinstallation:
- Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/linux/).
- Install Python 3.12
```
sudo apt-get install python3
sudo apt-get upgrade -y && sudo apt-get update -y
```

## Installation
#### 1. Clone the repository:
   ```
   git clone https://github.com/TimofeyDE/web_tracking_system.git
   ```
#### 2. Move to the directory:
   ```
   cd web_tracking_system
   ```
#### 3. To run the deployment of the server:
> Docker container is started in the background mode.
   ```
   ./server_deployment
   ```
#### 4. If you need to deploy the client side:
> The client is created as a daemon and started automatically when the system is boot up.
   ```
   sudo ./client_deployment
   ```
