from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninjas import Ninja
from pprint import pprint

# === C R U D ===

# model the class after the friend table from our database
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    #! all queries are classmethods
        
    #* =========== READ ALL ===========
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print("==========================",results)
        pass
        dojos_instances = []
        if results:
            for row in results:
                one_dojo = Dojo(row)
                dojos_instances.append(one_dojo)
        return dojos_instances
    

        #* =========== READ one by id ===========
    @classmethod
    def get_one_dojo(cls,data):
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s ; 
                """
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        print(dojos)
        return dojos






    #* =========== CREATE to create a new dojo===========

    @classmethod
    def add_dojo(cls, data):

        query = """
                INSERT INTO dojos (name)
                VALUES (%(name)s);
                """
        
        result = connectToMySQL(DATABASE).query_db(query, data)
        print("The id of the created car is: ", result)
        return result
    
#* =========== show dojo and his ninjas===========

    
    @classmethod
    def get_one_dojo_ninjas(cls, data):

        query = """
                    SELECT * FROM dojos
                    JOIN ninjas ON dojos.id = ninjas.dojo_id
                    WHERE dojos.id = %(id)s;
                """
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        # pprint(results)
        this_dojo = cls(results[0])
        
        all_ninjas = []
        for one_ninja in results:
            fixed_ninja_data = {
                **one_ninja,
                "id" : one_ninja["ninjas.id"],
                "created_at": one_ninja["ninjas.created_at"],
                "updated_at": one_ninja["ninjas.updated_at"]
            }
            all_ninjas.append(Ninja(fixed_ninja_data))
        
        this_dojo.ninjas = all_ninjas
        # pprint(this_dojo)
        return this_dojo