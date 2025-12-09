from app import app
from flask import jsonify, request

from services.logger import logger

@app.route('/log/file', methods=['POST'])
def log():
  data_from_req = request.get_json()
  if "msg" not in data_from_req:
    return jsonify(data={ "isLogged": False, "Message": "" }, status=400)

  isLogged = logger(data_from_req["msg"])
  
  return jsonify(data={ "isLogged": isLogged, "Message": data_from_req["msg"] }, status=200)
