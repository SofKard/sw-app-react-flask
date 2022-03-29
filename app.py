from flask import Flask, jsonify
from flask.helpers import send_from_directory
app = Flask(__name__, static_folder='./ui/build', static_url_path='/') # where static files are stored
# static_url_path is seen in front end, static_folder seen in backend 

# comment out on deployment
#from flask_cors import CORS
#CORS(app)

if __name__ == 'main':
    app.run()

# function to take input form frontend and test against "Sofie"
@app.route("/input/<fname>", methods=["GET"])
def input(fname: str):
    print("fname=", fname)
    if fname == "Sofie":
        output = "Kardonik"
    else:
        output = "First Name Not Found"
    print("out=", output)
    return jsonify(str=output)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")
    # return app.send_static_file('index.html')
