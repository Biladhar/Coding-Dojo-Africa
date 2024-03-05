from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninjas import Ninja
from flask_app.models import dojos

# * view route

@app.route("/ninjas")
def ninja_form():
    return render_template("form.html",dojos=dojos.Dojo.get_all())


#! Action Route too add new dojo
@app.route("/ninja/new", methods=["POST"])
def add_ninja():
    print("**********",request.form)
    Ninja.new_ninja(request.form)
    #! NEVER EVER EVER render on a post request
    return redirect("/dojos")