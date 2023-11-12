from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import win32com.client
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__, static_folder='../dist', static_url_path='/')
CORS(app)

logging.basicConfig(level=logging.INFO)
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Create the HouseBot external control object
hb = win32com.client.Dispatch("HBControlMod.HBControl")
hb.Connect("5010", "127.0.0.1", "123")


def fix_heb_encoding(encoded_str, reverse=False):
    encodings = ['latin-1', 'windows-1255']

    if reverse:
        encodings.reverse()

    try:
        encoded_bytes = encoded_str.encode(encodings[0])
        return encoded_bytes.decode(encodings[1])
    except (Exception,):
        return encoded_str


@app.route('/execute-task', methods=['POST'])
def execute_task():
    data = request.get_json()
    task_name = data.get('name')
    if not task_name:
        return jsonify({'error': 'Task name not provided'}), 400

    hb.ExecuteTask(task_name)
    return jsonify({'message': 'Task executed successfully'})


@app.route('/set-property', methods=['POST'])
def set_property():
    data = request.get_json()
    device = data.get('device')
    property = data.get('property')
    value = data.get('value')

    device = fix_heb_encoding(device, True)
    property = fix_heb_encoding(property, True)

    app.logger.info(f"Setting property: {property} on device: {device} to value: {value}")
    hb.SetPropertyValue(device, property, value)

    return jsonify({'message': 'Property changed successfully'})


@app.route('/get-property', methods=['GET'])
def get_property():
    device = request.args.get('device')
    property = request.args.get('property')

    device = fix_heb_encoding(device, True)
    property = fix_heb_encoding(property, True)

    value = hb.GetPropertyValue(device, property)
    app.logger.info(f"Retrived property: {property} on device: {device} = {value}")

    return jsonify({'value': value})


@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    res = hb.GetTaskList(";")
    res = fix_heb_encoding(res)

    return jsonify({'values': res.split(";")})


@app.route('/get-devices', methods=['GET'])
def get_devices():
    res = hb.GetDeviceList(";")
    res = fix_heb_encoding(res)

    return jsonify({'values': res.split(";")})


@app.route('/get-device-properties', methods=['GET'])
def get_device_properties():
    device = request.args.get('device')
    res = hb.GetPropertyListForDevice(device, ";")
    res = fix_heb_encoding(res)

    return jsonify({'values': res.split(";")})


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def fallback(e):
    return send_from_directory(app.static_folder, 'index.html'), 200


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
