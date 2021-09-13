from flask import Flask, render_template,redirect,request,session
# import the class from friend.py
from users import User
app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()


    print(users)
    return render_template("read.html", users = users)


@app.route("/form")
def form():
    # call the get all classmethod to get all friends
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
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={ 
        "id":id
    }
    return render_template("delete.html",user=User.get_one(data))


@app.route('/user/delete_all/<int:id>')
def delete_all(id):
    data ={
        'id': id
    }
    User.delete_all(data)
    return redirect('/users')

if __name__ == "__main__":
        app.run(debug=True)
