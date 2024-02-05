#!/bin/bash

# The directory of the project itself
PROJECT_DIR=$(dirname "$0")

LOG_FILE="client.log"

START_SCRIPT="$(realpath $PROJECT_DIR)/test/client.py"
SERVICE_FILE="/etc/systemd/system/client.service"
USER=$(whoami)

sudo tee "$SERVICE_FILE" > /dev/null << EOF
[Unit]
Description=Client App Service
After=network.target

[Service]
Type=simple
User=$USER
Environemnt
WorkingDirectory=$(realpath $PROJECT_DIR)
ExecStart=/usr/bin/python3 $START_SCRIPT
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable client.service
sudo systemctl start client.service

echo "Client service setup complete. Use 'systemctl status client.service' to check the service status"