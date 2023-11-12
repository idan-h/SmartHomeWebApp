from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import win32com.client

app = Flask(__name__, static_folder='../dist', static_url_path='/')
CORS(app)

# Create the HouseBot external control object
hb = win32com.client.Dispatch("HBControlMod.HBControl")
hb.Connect("5010", "127.0.0.1", "123")


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

    hb.SetPropertyValue(device, property, value)
    return jsonify({'message': 'Property changed successfully'})


@app.route('/get-property', methods=['GET'])
def get_property():
	device = request.args.get('device')
	property = request.args.get('property')

	value = hb.GetPropertyValue(device, property)
	return jsonify({'value': value})


@app.route('/get-tasks', methods=['GET'])
def get_tasks():
    res = hb.GetTaskList(";")
    return jsonify({'values': res.split(";")})


@app.route('/get-devices', methods=['GET'])
def get_devices():
	res = hb.GetDeviceList(";")
	return jsonify({'values': res.split(";")})


@app.route('/get-device-properties', methods=['GET'])
def get_device_properties():
	device = request.args.get('device')
	res = hb.GetPropertyListForDevice(device, ";")
	return jsonify({'values': res.split(";")})


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.errorhandler(404)
def fallback(e):
    return send_from_directory(app.static_folder, 'index.html'), 200


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
