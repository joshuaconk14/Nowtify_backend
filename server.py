from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__) # create app instance / representation
CORS(app)

# # API test route
# @app.route("/members")
# def members():
#     return {"members": ["members1", "members2", "members3"]}

# login route and defining home page
@app.route("/home")
def home():
    return jsonify("Welcome to Nowtify!")



# run flask app
if __name__ == "__main__":
    app.run(port = 5000, debug = True)