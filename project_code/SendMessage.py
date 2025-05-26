import DBManager

class SendMessage:
    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver

    def sendMsg(self):
        db = DBManager.DBManager(database="petato_db")
        db.connect()
        db.execute_query(
            "INSERT INTO messages (msg_sender, msg_receiver, msg_text) VALUES (%s, %s, %s)", 
            (self.sender, self.receiver, self.message)
        )
        db.connection.commit()

            
        db.close()
