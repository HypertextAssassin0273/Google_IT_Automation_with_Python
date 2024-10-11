#!/usr/bin/env python3

import requests, socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    return response == 200
