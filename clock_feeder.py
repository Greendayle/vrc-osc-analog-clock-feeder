#!/bin/env python3
from pythonosc import udp_client
import time
client_osc = udp_client.SimpleUDPClient("127.0.0.1", 9000)

while True:
    hour, minute = time.strftime('%H %M').split()
    hours_send = float(int(hour) % 12) / 12 + float(int(minute) / 60 / 12)
    minute_send = float(minute) / 60
    
    client_osc.send_message("/avatar/parameters/hour", hours_send)
    client_osc.send_message("/avatar/parameters/minute", minute_send)
    time.sleep(1.0)
