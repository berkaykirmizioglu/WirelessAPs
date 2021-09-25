import time
from multiprocessing.connection import Listener

from alert import alert_changes
from utils.json_utils import read_from_json

listener = Listener(('localhost', 6000), authkey=b'WirelessAP')

app_on: bool = True
check_interval: int = 10


def start_server():
    while app_on:
        conn = listener.accept()
        print('New connections can be received!', listener.last_accepted)

        previous = read_from_json("access_points.json")

        while True:
            message = conn.recv()
            current = read_from_json("access_points.json")
            conn.send(alert_changes(previous, current))
            previous = current
            time.sleep(check_interval)
            print(message)
            listener.close()


start_server()
