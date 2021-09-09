from extensions import db

class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())

    def __repr__(self):
        return f'{self.id}, {self.title}, {self.description}'

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()




