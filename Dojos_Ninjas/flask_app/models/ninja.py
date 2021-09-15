from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_ID) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_ID)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)