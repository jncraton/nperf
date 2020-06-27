from urllib import request

def is_internet_up():
    """ Checks if we have access to the Internet

    This uses the same HTTP request that Android uses to confirm connectivity

    This requires valid DNS and a working connection to the external host. 

    >>> is_internet_up()
    True
    """
    
    res = request.urlopen('http://connectivitycheck.gstatic.com/generate_204')

    return res.getcode() == 204
