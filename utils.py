from subprocess import check_output


def get_ip_address():
    ips = check_output(['hostname', '--all-ip-addresses'])
    return [ip for ip in ips.split(' ') if '192.168.' in ip][0]