from flask_app.models.user import User
from flask_app import app
from flask import render_template, redirect, session, request, flash
from werkzeug.utils import validate_arguments

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
# which is made by invoking the function Bcrypt with our app as an argument



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        "password": pw_hash
    }
    # Call the save @classmethod on User
    user_id = User.register_user(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/dashboard")

# ************************
# login Route 
# *************************
@app.route("/login", methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)

    data = {
        "user" : user_in_db,
        "password" : request.form['password']
    }
    if not User.validate_login(data):
        return redirect("/")
    
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")

@app.route ("/dashboard")
def dashboard():
        if not "user_id"  in session:
            return redirect("/")

        data = {
            "id" : session['user_id']
        }
        user = User.get_by_id(data)
        return render_template("dashboard.html", user = user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")