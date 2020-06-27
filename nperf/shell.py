from subprocess import check_output
import re

def get_default_gateway():
    """ Returns the current default gateway
    
    >>> get_default_gateway() # doctest: +SKIP
    '192.168.1.1'
    """

    output = check_output(['ip','route','show']).decode('utf8')
    return re.search('default via ([\d\.]+)', output).group(1)

def check_ping(host='8.8.8.8', timeout=1):
    """ Checks the ICMP roundtrip ping time to a hosts

    Returns ping time in milliseconds

    >>> check_ping("1.1.1.1") # doctest: +SKIP
    4.5

    >>> check_ping("1.1.1.1") > 0
    True

    >>> check_ping() > 0
    True

    >>> check_ping("1.1.1.1") < 100
    True

    >>> check_ping() < 100
    True
    """

    output = check_output(['ping', '-c', '1', '-W', str(timeout), host]).decode('utf8')
    return float(re.search('time\=([\d\.]+)', output).group(1))
