from flask import Flask, render_template
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
    return render_template('home.html')



# run flask app
if __name__ == "__main__":
    app.run(port = 5000, debug = True)