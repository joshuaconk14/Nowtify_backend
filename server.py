from flask import Flask

app = Flask(__name__) # create app instance / representation

# API route
@app.route("/members")
def members():
    return {"members": ["members1", "members2", "members3"]}


# run flask app
if __name__ == "__main__":
    app.run(port = 5000, debug = True)