#!flask/bin/python
from flask import Flask
from messages import add
app = Flask(__name__)


@app.route('/')
def index():
    add.delay(4, 4)
    return 'accepted', 'HTTP/1.1 202 Accepted'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
