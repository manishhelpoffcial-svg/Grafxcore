from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='Grafxcore-V1zip/agency-site')

@app.route('/')
def serve_index():
    return send_from_directory('Grafxcore-V1zip/agency-site', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('Grafxcore-V1zip/agency-site', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
