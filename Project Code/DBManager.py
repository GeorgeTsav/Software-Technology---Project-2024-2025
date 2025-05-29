import mariadb

class DBManager:
    def __init__(self, host='localhost', user='root', password='', database='petato_db'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection successful.")
        except mariadb.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def execute_query(self, query, params=None):
        if not self.connection:
            print("No connection established.")
            return None
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            return cursor
        except mariadb.Error as err:
            print(f"Error: {err}")
            return None

if __name__ == "__main__":
    db = DBManager(host='localhost', user='root', password='', database='petato_db')
    db.connect()