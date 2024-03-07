from flask_app.configs.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from pprint import pprint
from flask import flash
from flask_app.models import users





class Recipe:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.date_cooked = data["date_cooked"]
        self.under = data["under"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


#* show all recipes
    @classmethod
    def show_all_recipe(cls):
        query = """
                SELECT * FROM recipes;
                """
        return connectToMySQL(DATABASE).query_db(query)
    


    # * add a recipe in the db
    @classmethod
    def add_recipe(cls,data):
        query = """
                INSERT INTO recipes (name, description, instruction, date_cooked, under, user_id)
                VALUES (%(name)s, %(description)s, %(instruction)s, %(date_cooked)s, %(under)s, %(user_id)s)
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    


    # * show all recipe with there poster
    @classmethod
    def show_all_recipe_with_users(cls):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                """
        results = connectToMySQL(DATABASE).query_db(query)
        list_of_recipes = []
        for row in results:
            current_recipe = Recipe(row)
            user_fix ={                                        # * to fix the data of users in the dic
                    **row,
                    "id" : row["users.id"],
                    "created_at" : row["users.created_at"],
                    "updated_at" : row["users.updated_at"]
            }
            current_recipe.posted_by = users.User(user_fix)          #* parzing after calling the users model  we add an atribute "posted-by" to the books to have acces to the users
            list_of_recipes.append(current_recipe)   
        return list_of_recipes
    


    # to get one recipe with the user that post it
    @classmethod
    def get_one_with_user(cls, data):
        query = """
                SELECT * FROM recipes
                JOIN users ON recipes.user_id = users.id
                WHERE recipes.id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        row = result[0]
        current_recipe = Recipe(row)
        recipe_user_fix ={                                        # * to fix the data of users in the dic
            **row,
            "id" : row["users.id"],
            "created_at" : row["users.created_at"],
            "updated_at" : row["users.updated_at"]
            }
        current_recipe.posted_by=users.User(recipe_user_fix)
        return current_recipe
    



    # * get one book by id
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recipes
                WHERE recipes.id = %(id)s;
                """
        result = connectToMySQL(DATABASE).query_db(query, data)
        pprint(result)                                  
        return Recipe(result[0])    


   # * method to update a recipe
    @classmethod
    def update(cls,data):
        query = """
                UPDATE recipes
                SET name = %(name)s,
                description= %(description)s,
                instruction = %(instruction)s,
                under = %(under)s,
                date_cooked = %(date_cooked)s
                WHERE recipes.id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query, data)
    

    # * method to delete a recipe
    @classmethod
    def delete(cls,data):
        query = """
                Delete From recipes
                WHERE id = %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query, data)  




    # ! validation for recipes
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data["name"]) < 3:
            is_valid = False
            flash("Name is required !", "recipe")

        if len(data["description"]) < 3:
            is_valid = False
            flash("Description is required !", "recipe")

        if len(data["instruction"]) < 3:
            is_valid = False
            flash("Instructions are required !", "recipe")

        if len(data["date_cooked"]) < 1:
            is_valid = False
            flash("Date when cooked is required !", "recipe")

        if len(data["under"]) < 1:
            is_valid = False
            flash("Under 30 min is required !", "recipe")

        return is_valid
