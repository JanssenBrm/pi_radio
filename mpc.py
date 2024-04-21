import subprocess
import logging
from time import sleep

MAX_RETRIES = 5
def mpc_command(cmd, attempt = 1):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return p.stdout.read()
    except Exception as error:
        logging.error(f'Cannot execute MPC command: {error}')
        if attempt < MAX_RETRIES:
            sleep(5)
            return mpc_command(cmd, attempt + 1)
        return None


def mpc_get_position():
    cmd = ['mpc', '-f', '%position%']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    position = p.stdout.read()
    idx = str(position).replace('\\n', '').replace('b\'', '').split('[')
    return None if len(idx) == 1 else int(str(idx[0]).strip())
