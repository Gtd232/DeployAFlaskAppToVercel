from PIL import Image
from flask import *
import random
from io import *

app = Flask(__name__)


@app.route("/colorful_venti", methods=["get"])
def api_colorful_venti():
    return '1'

@app.route("/", methods=["get"])
def api_colorful_ventis():
    return '1'

@app.route("/s", methods=["get"])
def api_colorful_vensti():
    return '1'

if __name__ == "__main__":
    app.run(port=14514, debug=True)
    
