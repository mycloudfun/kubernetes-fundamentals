from flask import Flask
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
    f = open('website.html', 'r')
    file_contents = f.read()
    return file_contents
    f.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
