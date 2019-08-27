from flask import Flask, jsonify
import socket
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/website')
def website_open():
    f = open('/data/website.html', 'r')
    file_contents = f.read()
    return file_contents
    f.close()

@app.route('/info')
def info():
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        return jsonify({'Hostname': host_name, 'IP': host_ip }), 200
    except: 
        return jsonify ({'Message': 'Unable to get Hostname and IP'}), 500 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
