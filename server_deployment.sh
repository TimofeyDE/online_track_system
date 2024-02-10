#!/bin/bash

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 -f[foreground] or -b[background]"
    exit 1
fi

while getopts "fb" OPT;
do
    case "${OPT}" in
        f)
            sudo docker-compose pull
            sudo docker-compose build
            sudo docker-compose up
            exit 0
            ;;
        b)
            sudo docker-compose pull -q

            # Build a Docker in background
            sudo docker-compose build -q

            # Run a Docker in background
            sudo docker-compose up -d
            exit 0
            ;;
        *)
            exit 1
            ;;
    esac
done

