from flask import  render_template,redirect,request,session

from flask_app import app
from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()


    print(users)
    return render_template("read.html", users = users)


@app.route("/form")
def form():
    return render_template("create.html")


@app.route("/add", methods = ['POST'])
def add():
    
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    user = User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')
    
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("editpage.html",user=User.get_one(data))

@app.route("/edit", methods = ['POST'])
def editpage():
    # call the get all classmethod to get all friends
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')


@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/user')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={ 
        "id" : id
    }
    user = User.delete(data)
    return redirect("/")



