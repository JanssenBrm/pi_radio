from flask import Flask
from flask import render_template
from flask import request
import subprocess

from mpc import mpc_command
from utils import get_ip_address

app = Flask(__name__)


@app.route("/")
def show_home():
    return render_template('radio.html')


@app.route("/play", methods=['GET'])
def play_radio():
    mpc_command(['mpc', 'play'])
    return "ACK"

@app.route("/stop", methods=['GET'])
def stop_radio():
    mpc_command(['mpc', 'stop'])
    return "ACK"


if __name__ == "__main__":
    app.run(host=get_ip_address())
