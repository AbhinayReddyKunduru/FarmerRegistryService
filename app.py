
import sqlite3
from flask import Flask, render_template, request, url_for, redirect,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'farmer_registry'
mysql = MySQL(app)


# L = list()
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home",methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/login",methods=['GET','POST'])
def login():
    # connection = sqlite3.connect('identifier.sqlite')
    error = None

    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute(''' SELECT * FROM SINEUP''')
        users = cur.fetchall()

        # cur = connection.cursor()
        # cur.execute("SELECT * FROM SINEUP")
        # users = cur.fetchall()

        for user in users:
            if request.form['Email'] == user[0] and request.form['password'] == user[1]:
                mysql.connection.commit()
                cur.close()
                return redirect('/home')

        error = 'Invalid credintials Try again'

    return render_template('login.html', error=error)

@app.route('/sineup',methods=['POST','GET'])
def sineup():

    if request.method =='POST':
        cur = mysql.connection.cursor()

        cur.execute(''' INSERT INTO SINEUP VALUES( %s, %s)''',(request.form['Email'], request.form['password']))
        
        # "INSERT INTO SINEUP VALUES (?,?)", (request.form['Email'], request.form['password'])

        mysql.connection.commit()
        cur.close()


        return redirect('/login')

    return render_template('sineup.html')


@app.route('/farmer', methods=['POST','PUT','GET'])
def create_farmer():

    # print(request.content_type)



    cur = mysql.connection.cursor()

    if request.method == 'PUT':

        # print(content)
        content = request.json
        cur.execute("""UPDATE FARMER_DETAILS SET FARMER_NAME= %s, MOBILE_NUMBER =%s,VILLAGE_NAME =%s, ADDRESS=%s WHERE FARMER_ID=%s""",
                    (content['FARMER_NAME'],content['MOBILE_NUMBER'],content['VILLAGE'],content['ADDRESS'],content['FARMER_ID']))

    elif request.method == 'POST':
        if request.content_type =='application/json':

            content = request.json
            cur.execute("""INSERT INTO FARMER_DETAILS VALUES(%s, %s, %s, %s, %s) """,
                    (content['FARMER_ID'],content['FARMER_NAME'],content['MOBILE_NUMBER'],content['VILLAGE'],content['ADDRESS']))
        else:
            cur.execute("""INSERT INTO FARMER_DETAILS VALUES(%s,%s,%s, %s, %s) """,
                        (request.form['FARMER_ID'],request.form['FARMER_NAME'],request.form['MOBILE_NUMBER'] ,request.form['VILLAGE'],request.form['ADDRESS']))

    else:
        return render_template('create_farmer.html')

    mysql.connection.commit()
    cur.close()

    return jsonify("Succss")

@app.route('/get_farmer_data', methods=['GET'])
def farmer_details():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM FARMER_DETAILS""")
    rows = cur.fetchall()

    mysql.connection.commit()
    cur.close()
    return render_template('farmer_details.html', items=rows)

















