from app import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256))
    phone = db.Column(db.String(256))

    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"{self.name}:{self.id}"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.emai,
            "phone": self.phone
        }
