import requests as req
import getmac
from datetime import datetime
import time

HOST = "127.0.0.1"
PORT = 5000
URL = f"http://{HOST}:{PORT}"



def send_status(mac_address):
    endpoint = f"{URL}/update"

    params = {
        "mac_address" : mac_address,
        "status" : "online",
        "last_online" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        response = req.post(endpoint, json=params)
    except req.exceptions.RequestException as e:
        print(f"Error sending request: {e}")


def main():
    mac_address = getmac.get_mac_address()
    
    while True:
        
        send_status(mac_address)
        time.sleep(60)
        

if __name__ == "__main__":
    main()
