#!flask/bin/python
from flask import Flask, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def route_all(path):
    try:
        path = request.path.split('/')
        loaded_mod = __import__('routing.' + request.method.lower() + '.' + path[1], fromlist=['accept'])
        endpoint = getattr(loaded_mod, 'accept')
        endpoint.delay(request.form, request.path)
        return '{"status":202,"message":"ACCEPTED"}', 'HTTP/1.1 202 Accepted'
    except AttributeError:
        return '{"status":404,"message":"NOT FOUND"}', 'HTTP/1.1 404 Not Found'

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
