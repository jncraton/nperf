from subprocess import call
import re

def ping(host):
    """ Pings a host

    >>> ping("1.1.1.1")
    1.0
    """

    call(['ping', '-c', 1, '-W', 1, host])
