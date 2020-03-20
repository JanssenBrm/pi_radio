import json
import os
from subprocess import check_output

from mpc import mpc_command


def get_ip_address():
    ips = check_output(['hostname', '--all-ip-addresses'])
    return [ip for ip in ips.split(' ') if '192.168.' in ip][0]

def get_stationlist():
    with open('{}/conf/stations.json'.format(os.path.dirname(os.path.abspath(__file__)))) as stations:
        return json.load(stations)['stations']

def reload_playlist():
    mpc_command(['mpc', 'clear'])
    for station in get_stationlist():
        mpc_command(['mpc', 'add', station['url']])
