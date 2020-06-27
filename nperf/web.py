from urllib import request
import socket
import time

def is_internet_up():
    """ Checks if we have access to the Internet

    This uses the same HTTP request that Android uses to confirm connectivity

    This requires valid DNS and a working connection to the external host. 

    >>> is_internet_up()
    True
    """
    
    res = request.urlopen('http://connectivitycheck.gstatic.com/generate_204')

    return res.getcode() == 204

def get_down_speed(timeout=.5):
    """
    Returns download speed in mbps

    Download speed is determined by downloading a test file from Softlayer using
    a single HTTP connection.

    `timeout` is used to set measurement duration
    
    >>> get_down_speed() > 1
    True
    """

    bytes = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('speedtest.wdc01.softlayer.com', 80))
        s.sendall(b'GET /downloads/test100.zip HTTP/1.1\r\nHost:speedtest.wdc01.softlayer.com\r\n\r\n')
        start = time.time()
        while time.time() < start + timeout:
            data = s.recv(1024 * 16)
            bytes += len(data)
    return 8 * bytes / timeout / 1024 / 1024
    