from ...mongo.connect import ConnectionMongo
import hashlib

class MongodUser:
    def __init__(self):
        self.connect = ConnectionMongo()

    def userConnect(self, user, pasw):
        db = self.connect.con
        col = db["credential"]  
        hash_object = hashlib.md5(pasw.encode())
        passw = hash_object.hexdigest()
        col = col.find_one({"user": user, "pasw": passw, "state": True}, {'_id': False})
        return col

