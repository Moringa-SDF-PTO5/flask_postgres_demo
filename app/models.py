from app import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author
        }