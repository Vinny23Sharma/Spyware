from db import db

class UserModel(db.Model):
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True)
    key_name = db.Column(db.String(100))
    data = db.Column(db.String(1000))

    def __init__(self, key_name, data):
        self.key_name = key_name
        self.data = data

    def json(self):
        return {'key':self.key_name, 'data': self.data}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
