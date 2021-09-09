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

class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    # addresses = db.relationship('Address', backref='person', lazy=True)

    def __repr__(self):
        return f'{self.id}, {self.content}'

    def __init__(self, content):
        self.content = content

    def save(self):
        db.session.add(self)
        db.session.commit()




