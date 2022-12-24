from flask import Flask, render_template, request, redirect, jsonify
from FarmerRegistryService.models.farmer import Farmer
from FarmerRegistryService.models.User import User_Cred
from FarmerRegistryService.dao.database import session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home():

    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        for user in session.query(User_Cred).all():
            if user.email == request.form['Email'] and user.password == request.form['password']:
                return redirect('/home')

        error = 'Invalid Creditions try again'

    return render_template('login.html', error=error)


@app.route("/sineup", methods=['GET', 'POST'])
def sineup():
    error = None
    if request.method == 'POST':

        email = request.form['Email']
        password = request.form['password']
        user = User_Cred(email, password)

        session.add(user)
        session.commit()

        return redirect('/login')

    return render_template('sineup.html', error=error)

@app.route("/farmer", methods=['GET', 'POST', 'PUT'])
def create_farmer():
    if request.method == 'PUT':
        content = request.json

        update_farmer = Farmer.query.filterby(farmer_id=content['FARMER_ID']).first()
        update_farmer.farmer_name = content['FARMER_NAME']
        update_farmer.mobile_number = content['MOBILE_NUMBER']
        update_farmer.village = content['MOBILE_NUMBER']
        update_farmer.address = content['ADDRESS']
        session.add(update_farmer)
        session.commit()
        return jsonify('Changes Done Sucessfully')

    elif request.method == 'POST':

        farmer = Farmer(request.form['FARMER_NAME'], request.form['MOBILE_NUMBER'], request.form['VILLAGE'],
                        request.form['ADDRESS'])

        session.add(farmer)
        session.commit()

        return jsonify('Submitted Sucessfully')

    return render_template('create_farmer.html')

@app.route("/get_farmer_data")
def farmer_details():
    farmers = session.query(Farmer).all()
    # print(farmers)

    return render_template('farmer_details.html', farmers=farmers)

if __name__ =="__main__":
        app.run(host="0.0.0.0", debug=True)
