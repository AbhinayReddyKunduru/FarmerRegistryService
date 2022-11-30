import sqlite3

from flask import Flask, request, jsonify, render_template,url_for,redirect
app = Flask(__name__)

L = list()
# Home Page for our website
@app.route("/")
def index():
    return render_template('index.html', name='PyCharm')

@app.route("/login",methods=['GET','POST'])
def login():
    connection = sqlite3.connect('identifier.sqlite')

    cur = connection.cursor()
    cur.execute("SELECT EMAIL FROM SINEUP")
    all_emails = cur.fetchall()


    error = None
    if request.method == 'POST':
        if tuple(request.form['Email']) not in all_emails or request.form['password'] != cur.execute("SELECT PASSWORD FROM SINEUP WHERE EMAIL=request.form['Email']").fetchall()[0][0]:
            error = 'Invalid credintials Try again'
        else:
            return redirect('/')
    return render_template('login.html', error=error)

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
def farmer_details():
    connection = sqlite3.connect('identifier.sqlite')

    cur = connection.cursor()
    cur.execute("SELECT * FROM FARMER_DETAILS")
    rows = cur.fetchall()
    return render_template('farmer_details.html', items=rows)




