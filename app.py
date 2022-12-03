import sqlite3

from flask import Flask, request, jsonify, render_template, redirect
app = Flask(__name__)

L = list()
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/home",methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
    connection = sqlite3.connect('identifier.sqlite')
    error = None

    if request.method == 'POST':
        cur = connection.cursor()
        cur.execute("SELECT * FROM SINEUP")
        users = cur.fetchall()

        for user in users:
            if request.form['Email'] == user[0] and request.form['password'] == user[1]:
                return redirect('/home')

        error = 'Invalid credintials Try again'

    return render_template('login.html', error=error)

@app.route('/sineup',methods=['POST','GET'])
def sineup():

    # print(type(request.content_type))
    connection = sqlite3.connect('identifier.sqlite')

    if request.method =='POST':
        cur = connection.cursor()
        cur.execute("INSERT INTO SINEUP VALUES (?,?)",(request.form['Email'],request.form['password']))
        connection.commit()
        connection.close()
        return redirect('/login')
    return render_template('sineup.html')


@app.route('/farmer', methods=['POST','PUT','GET'])
def create_farmer():

    # print(request.content_type)
    content = request.json
    # print(content)
    # L.append(content)
    # with open('schema.sql') as f:
    # connection.executescript(f.read())

    connection = sqlite3.connect('identifier.sqlite')
    cur = connection.cursor()

    if request.method == 'PUT':
        # print(content)
        cur.execute("UPDATE FARMER_DETAILS SET FARMER_NAME= ?, MOBILE_NUMBER =?,VILLAGE_NAME =?, ADDRESS=?  WHERE FARMER_ID=?",
                    (content['FARMER_NAME'],content['MOBILE_NUMBER'],content['VILLAGE'],content['ADDRESS'],content['FARMER_ID']))

    elif request.method == 'POST':
        if request.content_type =='application/json':
            cur.execute("INSERT INTO FARMER_DETAILS (FARMER_ID,FARMER_NAME,MOBILE_NUMBER,VILLAGE_NAME,ADDRESS) "
                    "VALUES (?, ?,?,?,?)",(content['FARMER_ID'],content['FARMER_NAME'],content['MOBILE_NUMBER'],content['VILLAGE'],content['ADDRESS']))
        else:
            cur.execute("INSERT INTO FARMER_DETAILS VALUES(?,?,?,?,?)",
                        (request.form['FARMER_ID'],request.form['FARMER_NAME'],request.form['MOBILE_NUMBER'] ,request.form['VILLAGE'],request.form['ADDRESS']))

    else:
        return render_template('create_farmer.html')

    connection.commit()
    connection.close()

    return jsonify("Succss")

@app.route('/get_farmer_data', methods=['GET'])
def farmer_details():
    connection = sqlite3.connect('identifier.sqlite')

    cur = connection.cursor()
    cur.execute("SELECT * FROM FARMER_DETAILS")
    rows = cur.fetchall()
    return render_template('farmer_details.html', items=rows)