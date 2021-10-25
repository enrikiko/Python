# Import the framework
from flask import Flask

# Create instace of flask
app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

class Device(object):
    def get(self):
        return "get"
    def post(self):
        return "post"

api.add_resource(Device, '/devices')
