import sqlite3

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

L = list()
@app.route("/")
def index():
    sql_query = 'SELECT * FROM FARMER_DETAILS;'
    curser = sqlite3.connect('identifier.sqlite')
    curser.execute(sql_query)


    return render_template('index.html', name='PyCharm')

@app.route('/farmer', methods=['POST'])
def create_farmer():
    content = request.json
    print(content)
    L.append(content)

    connection = sqlite3.connect('identifier.sqlite')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()
    for i in range(len(L)):
        cur.execute("INSERT INTO FARMER_DETAILS (FARMER_ID,FARMER_NAME,MOBILE_NUMBER,VILLAGE_NAME,ADDRESS) VALUES (?, ?,?,?,?)",(L[i]['FARMER_ID'],L[i]['FARMER_NAME'],L[i]['MOBILE_NUMBER'],L[i]['VILLAGE'],L[i]['ADDRESS']))
    connection.commit()
    connection.close()

    return jsonify("Succss")

@app.route('/get_farmer_data', methods=['GET'])
def send_data():
    return jsonify(L)


