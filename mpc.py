import subprocess


def mpc_command(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.stdout.read()

def mpc_get_position():
    cmd = ['mpc', '-f', '%position%']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    position = p.stdout.read()
    idx = str(position).replace('\\n', '').replace('b\'', '').split('[')
    return None if len(idx) == 1 else int(str(idx[0]).strip())
