from flask_app import app
from flask import redirect, render_template, request  , session
from flask_app.models.recipes_model import Recipe
from flask_app.models.users import User








# * view route ( Display the create a recipe form)
@app.route("/recipes/new")
def create_recipe_form():
    if "user_id" not in session:
        return redirect ("/")
    return render_template ("recipe_form.html")


# ! Action route (create a recipe)
@app.route("/recipe/process", methods=["POST"])
def process_new_recipe():
    # verify if user is logged
    if "user_id" not in session:
        return redirect ("/")
    # alert if the field are empty
    if not Recipe.validate_recipe(request.form):  
        return redirect("/recipes/new")
    # ? grab user id from session
    data = {                                    
        **request.form,                               
        "user_id" : session["user_id"]
    }
    # ? save the recipe in DB
    Recipe.add_recipe(data)                                        
    return redirect("/recipes")


# * VIEW ROUTE (dashboard)
@app.route("/recipes")
def display_all_recipes_with_users():
    # verify if user is logged
    if "user_id" not in session:
        return redirect ("/")
    # grab the user id from session and put in a dictionary
    data = {"id": session["user_id"]}
    # grab the user by id from DB
    current_user = User.get_by_id(data)
    # print("===> current_user:", current_user)
    all_recipes_users = Recipe.show_all_recipe_with_users()
    return render_template("dashboard.html", current_user = current_user , all_recipes = all_recipes_users )


# * VIEW ROUTE (to see one recipe)
@app.route("/recipes/<int:id>")
def display_one_recipe(id):
    if "user_id" not in session:
        return redirect ("/")
    recipe_id= { "id" : id  }                           # ! wee make a dictionary to send it to the model with the .get_by_id()
    one_recipes = Recipe.get_one_with_user(recipe_id)                   # ! tu luis envoi le book id sous format de dictionnaire                                             
    # grab the user id from session and put in a dictionary
    data = {"id": session["user_id"]}
    # grab the user by id from DB
    current_user = User.get_by_id(data)

    return render_template("one_recipe.html", recipe = one_recipes, current_user = current_user)


# * view route  (show form edit)
@app.route("/recipes/edit/<int:id>")
def display_edit_form(id):
    if "user_id" not in session:
        return redirect ("/")
    recipe_dict = {"id" : id}
    selected_recipe = Recipe.get_by_id(recipe_dict)
    return render_template("update_recipe.html",recipe=selected_recipe)

#! action route process the updated form
@app.route("/recipes/process/<int:id>", methods =["POST"])
def process_updated_recipe(id):
    if "user_id" not in session:
        return redirect ("/")
        # ? check if recipe is valid
    if not Recipe.validate_recipe(request.form):  # * (if not) ou ( if xxxxx == false )  #to see if the validation we make in model is true or false
        return redirect(f"/recipes/edit/{id}")
    # ? grab user id from session
    data = {                                    # * add a dictionary with user_id that we put in session in the login and registration , because the request.form didnt contain it 
        **request.form,                               # ! error something went wrong user_id
        "user_id" : session["user_id"],
        "id" : id
    }
    # print("==============>",data)  
    # ? save the recipe to db
    print(Recipe.update(data))
    return redirect("/recipes")


#! action route process delete
@app.route("/delete/<int:id>", methods =["POST"])
def delete_recipe(id):
    if "user_id" not in session:
        return redirect ("/")
    Recipe.delete({"id":id})
    return redirect("/recipes")