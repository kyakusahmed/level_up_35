

import psycopg2

class DatabaseConnection:

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database="postgres", user="postgres", password="1988", port="5432", host="localhost"
            )
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()
            print("connected")
        except Exception as ex:
            print("connection failed {}".format(ex))

    def get_users(self):
        command = """
        SELECT * FROM users
        """

        self.cursor.execute(command)
        return self.cursor.fetchall()

    def add_user(self,username,email,password):
        try:
            command = """
            INSERT INTO users (name, email, password) VALUES ('{}', '{}', '{}')
            """.format(username, email, password)
            self.cursor.execute(command)
            return "Data inserted"
        except Exception as ex:
            return "Failed {} ".format(ex)
