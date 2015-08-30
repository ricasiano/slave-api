#!flask/bin/python

# api.py
# routing for http API requests
# Author: Rai Icasiano <ricasiano at gmail dot com>

from flask import Flask, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def route_all(path):
    """ 
    Catch all http requests, route it to a specific endpoint and return 
    the appropriate http response if exists

    Keyword arguments:
    path -- the uri path, as documented in Flask http://flask.pocoo.org/snippets/57/
    """
    try:
        request_path = path.split('/')
        loaded_mod = __import__('routing.' + request.method.lower() + '.' + request_path[0], fromlist=['accept'])
        try: 
            endpoint = getattr(loaded_mod, 'accept')
            #async request to our endpoint
            endpoint.delay(request.form)
            return '{"status":202,"message":"ACCEPTED"}', 'HTTP/1.1 202 Accepted'

        except AttributeError:
            return '{"status":404,"message":"NOT FOUND"}', 'HTTP/1.1 404 Not Found'

    except ImportError:
        return '{"status":404,"message":"NOT FOUND"}', 'HTTP/1.1 404 Not Found'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
