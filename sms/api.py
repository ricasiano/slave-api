#!flask/bin/python
from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return '{"status":404,"message":"NOT FOUND"}', 'HTTP/1.1 404 Not Found'

#message endpoint, all inbound messages are rerouted here
@app.route('/message', methods=['POST'])
def message():
    from message import accept
    result = accept.delay(request.form)
    result.wait()
    return '{"status":202,"message":"ACCEPTED"}', 'HTTP/1.1 202 Accepted'

#notification if delivered or not, useful for multi-part messages
@app.route('/notification', methods=['POST'])
def notification():
    from notification import notification_accept
    result = notification_accept.delay(request.form)
    result.wait()
    return '{"status":202,"message":"ACCEPTED"}', 'HTTP/1.1 202 Accepted'

#if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
