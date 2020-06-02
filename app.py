from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import subprocess
import os

from mpc import mpc_command, mpc_get_position
from utils import get_ip_address, get_stationlist, reload_playlist

app = Flask('Radio PPJ')


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

@app.route("/status", methods=['GET'])
def get_status():
    position = mpc_get_position()
    status = {
        "volume": int(str(mpc_command(['mpc', 'volume'])).split(':')[1].replace('%\\n\'', '').strip()),
        "playing": True if mpc_command(['mpc', 'current']) else False,
        "radio": position
    }
    return jsonify(status)

@app.route("/stations", methods=['GET'])
def get_stations():
    return jsonify(get_stationlist())

@app.route("/stations/<string:position>", methods=['POST'])
def set_station(position):
    mpc_command(['mpc', 'play', position])
    return "ACK"

@app.route("/volume/<string:volume>", methods=['POST'])
def set_volume(volume):
    print(volume)
    mpc_command(['mpc', 'volume', volume])
    print(mpc_command(['mpc', 'volume']))
    return "ACK"

if __name__ == "__main__":
    reload_playlist()
    app.run(host=get_ip_address())

