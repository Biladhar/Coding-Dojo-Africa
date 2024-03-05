from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojos import Dojo 

#* View Route
@app.route("/dojos")
def home():
    all_dojos  = Dojo.get_all()
    return render_template("home.html", all_dojos=all_dojos)


#! Action Route too add new dojo
@app.route("/dojo/new", methods=["POST"])
def add_dojo():
    # print(request.form)
    Dojo.add_dojo(request.form)
    #! NEVER EVER EVER render on a post request
    return redirect("/dojos")


#* View Route
@app.route("/dojos/<int:id>")
def get_dojo_ninjas(id):
    #fetch dojo by id
    dojo_dict = {
    "id": id
    }
    this_dojo_ninjas = Dojo.get_one_dojo_ninjas(dojo_dict)

    return render_template("ninjas.html", this_dojo=this_dojo_ninjas)