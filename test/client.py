import os
import sys
from configparser import ConfigParser
import requests as req
import uuid
from datetime import datetime
import time
import logging
from logging.handlers import TimedRotatingFileHandler

 
logpath=os.path.join(os.path.abspath(os.curdir), "client.log")
log_handler = TimedRotatingFileHandler(logpath, when='H', interval=1)
logging.basicConfig(filename=logpath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger(logpath).addHandler(log_handler)


def send_status(url, mac_address):
    endpoint = f"{url}/update"

    params = {
        "mac_address" : mac_address,
        "status" : "online",
        "last_online" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        res = req.post(endpoint, json=params)
        logging.info(res.json())
    except req.exceptions.RequestException as e:
        logging.error(f"Sending request: {e}")


def handle_options() -> str:
    url = str()
    config = ConfigParser()

    filepath = os.path.join(os.path.realpath(os.curdir), "configs", "client.ini")

    config.read(filepath)
    host = config["SERVER-SIDE"]["host"]
    port = config["SERVER-SIDE"]["port"]
    return f"{host}:{port}"


def main():
    url = handle_options()

    # joins elements of getnode() after each 2 digits.
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    
    while True:
        send_status(url, mac_address)
        time.sleep(60)
        

if __name__ == "__main__":
    main()

