from application import db

class Projects(db.model):
	projectID = db.Column(db.Integer, primary_key=True)
	projectName = db.Column(db.String(100), nullable=False, unique=True)
	projectComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)

	def __repr__(self):
    return ''.join([
        'User ID: ', self.user_id, '\r\n',
        'Title: ', self.title, '\r\n', self.content
    ])

class Epics(db.model):
	epicID = db.Column(db.Integer, primary_key=True)
	projectID = db.Column(db.Integer, db.ForeignKey'Projects.projectID', nullable=False)
	epicName = db.Column(db.String(100), nullable=False, unique=True)
	epicComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)

	 def __repr__(self):
    return ''.join([
        'User ID: ', self.user_id, '\r\n',
        'Title: ', self.title, '\r\n', self.content
    ])

class UserStories(db.model):
	ustoryID = db.Column(db.Integer, primary_key=True)
	ustoryName = db.Column(db.String(100), nullable=False, unique=True)
	ustoryComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)

	def __repr__(self):
    return ''.join([
        'User ID: ', self.user_id, '\r\n',
        'Title: ', self.title, '\r\n', self.content
    ])