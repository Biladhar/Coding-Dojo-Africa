
from flask_app import app
from flask import render_template, redirect,request
from flask_app.models.users import User





@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("index.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("add_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')