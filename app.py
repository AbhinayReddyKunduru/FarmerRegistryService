from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from sqlalchemy.exc import DatabaseError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/farmer_registry1'
app.config['SQLALCEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# @app.errorhandler(exc.SQLAlchemyError)
# def handle_db_exceptions(error):
#     db.session.rollback()


class Farmer(db.Model):
    farmer_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    mobile_number = db.Column(db.String(100), unique=True)
    village_name = db.Column(db.String(100))
    address = db.Column(db.String(250))

    def __init__(self, username, mobile_number, village_name, address):
        self.username = username
        self.mobile_number = mobile_number
        self.village_name = village_name
        self.address = address

    def __repr__(self):
        return f'<user_name is {self.username}'


class User_Cred(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f'user mail is {self.email}'


class Fertilizers(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(300))
    unit_cost = db.Column(db.Float)
    supplier = db.Column(db.String(100))
    quantity = db.Column(db.Float)
    bags = db.Column(db.Integer)
    total_cost = db.Column(db.Float)

    def __init__(self, product_name, unit_cost, supplier, quantity, bags, total_cost):
        self.product_name = product_name
        self.unit_cost = unit_cost
        self.supplier = supplier
        self.quantity = quantity
        self.bags = bags
        self.total_cost = total_cost

    def __repr__(self):
        return f'<product_name is {self.product_name}>'


class Pestisides(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200))
    unit_cost = db.Column(db.Float)
    supplier = db.Column(db.String(200))
    unit_quantity = db.Column(db.Float)
    cottons = db.Column(db.Integer)
    total_cost = db.Column(db.Float)

    def __init__(self, product_name, unit_cost, supplier, unit_quantity, cottons, total_cost):
        self.unit_cost = unit_cost
        self.product_name = product_name
        self.total_cost = total_cost
        self.supplier = supplier
        self.unit_quantity = unit_quantity
        self.cottons = cottons

    def __repr__(self):
        return f'fertilizer name is {self.product_name}'


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
        for user in User_Cred.query.all():
            if user.email == request.form['Email'] and user.password == request.form['password']:
                return redirect('/home')

        error = 'Invalid Creditions try again'

    return render_template('login.html', error=error)


@app.route("/sineup", methods=['GET', 'POST'])
def sineup():
    error = None
    if request.method == 'POST':
        try:
            email = request.form['Email']
            password = request.form['password']
            user = User_Cred(email, password)
            db.session.add(user)
        except:
            error = 'Email Already Exists try with another'
            db.session.rollback()
            # raise
        else:
            db.session.commit()
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

        db.session.commit()
        return jsonify('Changes Done Sucessfully')

    elif request.method == 'POST':

        farmer = Farmer(request.form['FARMER_NAME'], request.form['MOBILE_NUMBER'], request.form['VILLAGE'],
                        request.form['ADDRESS'])
        try:
            db.session.add(farmer)
        except DatabaseError:
            db.session.rollback()
            raise
        else:
            db.session.commit()
            return jsonify('Submitted Sucessfully')

    return render_template('create_farmer.html')


@app.route("/get_farmer_data")
def farmer_details():
    farmers = Farmer.query.all()

    return render_template('farmer_details.html', farmers=farmers)

