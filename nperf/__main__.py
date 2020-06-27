from nperf.web import get_down_speed
from nperf.shell import check_ping, get_default_gateway

def main():
 print(f'Local latency: {check_ping(get_default_gateway()):.02f}ms')
 print(f'Internet latency: {check_ping():.02f}ms')
 print(f'Internet bandwidth {get_down_speed():.02f}mbps')