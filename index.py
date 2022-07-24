from flask import *


app = Flask(__name__)


@app.route("/")
def TFGS():
    return '唔唔唔'


if __name__ == "__main__":
    app.run(port=14514, debug=True)
    
