from multiprocessing.connection import Client
import time

conn = Client(('localhost', 6000), authkey=b'WirelessAP')

client_on: bool = True
check_interval: int = 5


def start_client():
    while True:
        try:
            conn.send('Getting Changes...')
            conn.recv()
            time.sleep(check_interval)
        except ConnectionRefusedError as cre:
            print("Start server first!", cre)


start_client()
