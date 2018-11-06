from flask import Flask, jsonify
import math
app = Flask(__name__)

@app.route("/name", methods= ["GET"])
def name():
    """
    Returns a jsonified dictionary containing name.
    """
    return jsonify({"name": "Haeryn"})

@app.route("/hello/<name>", methods= ["GET"])
def hello(name):
    """
    Returns a greeting message to user-specified name.
    """
    return jsonify({"message": "Hello there, {}".format(name)})

@app.route("/distance", methods= ["POST"])
def distance():
    """
    Returns computation of distance between two points.
    """
    r = requests.get_json()
    x = r["a"][0] - r["b"][0]
    y = r["a"][1] - r["b"][1]
    s = math.sqrt(x^2 + y^2)
    r["distance"]= s
    return jsonify(r)
