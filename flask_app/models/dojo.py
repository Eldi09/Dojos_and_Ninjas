from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db_name = "dojo_and_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.db_name).query_db(query)
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES(%(name)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def ninjas_of_dojo(cls, data):
        query = "SELECT ninjas.first_name, ninjas.last_name, ninjas.age FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojos_id WHERE ninjas.dojos_id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results