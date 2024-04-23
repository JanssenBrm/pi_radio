import logging

from flask import Flask
from flask import jsonify
from flask import render_template

from mpc import mpc_get_position, mpc_command
from utils import get_stationlist, reload_playlist

logging.basicConfig(filename='pyradio.log', encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
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
    try:
        position = mpc_get_position()
        status = {
            "volume": int(str(mpc_command(['mpc', 'volume'])).split(':')[1].replace('%\\n\'', '').strip()),
            "playing": True if mpc_command(['mpc', 'current']) else False,
            "radio": position,
            "error": ""
        }
    except Exception as error:
        logging.error(f'Cannot retrieve status: {error}')
        status = {
            "error": str(error),
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
    app.run(host='0.0.0.0', port=5000)
