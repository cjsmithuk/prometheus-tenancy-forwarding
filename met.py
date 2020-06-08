#!/bin/env python3
#
# met.py - expose a sample metrics endpoint
#

from prometheus_client import start_http_server, Summary
import random
import argparse
import sys
import time

# Create metric
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing_requiests')

@REQUEST_TIME.time()
def process_request(t):
    """Do some stuff that takes 0.0->1.0 seconds"""
    time.sleep(t)

def metrics_server(n):
    port = int('902' + str(n))
    start_http_server(port)
    while True:
        process_request(random.random())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: met.py N")
    else:
        metrics_server(sys.argv[1])