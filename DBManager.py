import mysql.connector

class DBManager:
    def __init__(self, host='localhost', user='root', password='', database='petato_db'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection successful.")
        except mysql.connector.Error as err:
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
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None


       #ADD REVIEW
    def add_review(self, review_text, stars, reviewer_username, reviewed_username):
        if not self.connection:
            print("No connection.")
            return False

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO review (rev_text, rev_score, rev_writer, rev_user)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (review_text, stars, reviewer_username, reviewed_username))
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error inserting review: {err}")
            return False

if __name__ == "__main__":
    db = DBManager(host='localhost', user='root', password='', database='petato_db')
    db.connect()    