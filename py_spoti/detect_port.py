import serial.tools.list_ports
from pprint import pprint

ports = serial.tools.list_ports.grep('/arduino/')

for port, desc, hwid in sorted(ports):
    # if 'arduino' not in 'desc':
    #     continue
    pprint("{}: {} [{}]".format(port, desc, hwid))
