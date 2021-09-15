from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    dojos= dojo.Dojo.get_all()
    print(dojos)
    return render_template('ninja.html',dojos= dojos)


@app.route('/add',methods=['POST'])
def add_ninja():
    print(request.form)
    ninja.Ninja.save(request.form)
    return redirect('/dojos')