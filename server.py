import json
import service.validateUser as vl

from flask.globals import request
from flask import Flask
from utils.baseresponse import BaseResponse

app = Flask(__name__)

# config file
fileConfig = open("config/config.json")
config = json.load(fileConfig)

@app.route('/validate-user', methods=["POST"])
def validateUser():
   body = request.get_json()
   result = vl.validateUserData(body)
   return BaseResponse.generateBaseResponse(
        data=result, responseCode=200, responseMessage="success"
    )

@app.route('/test')
def hello_world():
   return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, port=config["port"], host="0.0.0.0")
