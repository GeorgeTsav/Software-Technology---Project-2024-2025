import DBManager
class SendMessage:
    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def sendMsg(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        try:
            query = "INSERT INTO messages (msg_sender, msg_receiver, msg_text, msg_date)VALUES (%s, %s, %s, NOW())"
            params = (self.sender, self.receiver, self.message)
            db.execute_query(query, params)
            db.connection.commit()
        except Exception as e:
            print("Error sending message:", e)
            
            
        db.close()
        