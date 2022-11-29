from flask import Flask, request, jsonify

app = Flask(__name__)
L = list()

@app.route("/")
def hello_world():
    return "<h1>Farmers Registry!</h1>"

@app.route('/farmer', methods=['POST'])
def create_farmer():
    content = request.json
    print(content)
    L.append(content)
    return jsonify("Succss")

# @app.route('/get_farmer_data')
# def send_data():
#     return jsonify()