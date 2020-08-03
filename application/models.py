from application import db

class Projects(db.model):
	projectID = db.Column(db.Integer, primary_key=True)
	projectName = db.Column(db.String(100), nullable=False, unique=True)
	projectComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)
	epics = db.relationship('Epics', backref='project', lazy=True)

	def __repr__(self):
		return ''.join([
			'Project ID: ', self.projectID, '\r\n',
			'Project Name: ', self.projectName, '\r\n'
		])

class Epics(db.model):
	epicID = db.Column(db.Integer, primary_key=True)
	projectID = db.Column(db.Integer, db.ForeignKey('Projects.projectID'), nullable=False)
	epicName = db.Column(db.String(100), nullable=False, unique=True)
	epicDesc = db.Column(db.String(100), nullable=False, unique=True)
	epicComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)
	ustories = db.relationship('User Stories', backref='epic', lazy=True)

	def __repr__(self):
		return ''.join([
			'Epic ID: ', self.epicID, '\r\n',
			'Epic Name: ', self.epicName, '\r\n'
		])

class UserStories(db.model):
	ustoryID = db.Column(db.Integer, primary_key=True)
	epicID = db.Column(db.Integer, db.ForeignKey('Epics.epicID'), nullable=False)
	ustoryName = db.Column(db.String(100), nullable=False, unique=True)
	ustoryComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)
	ustoryAsA = db.Column(db.String(500), nullable=False, unique=True)
	ustoryIWant = db.Column(db.String(500), nullable=False, unique=True)
	ustoryToSo = db.Column(db.String(500), nullable=False, unique=True)

	def __repr__(self):
		return ''.join([
			'User Story ID: ', self.user_id, '\r\n',
			'User Story Name: ', self.title, '\r\n', 
			'As A: ',
			'I Want: ',
			'To/So: ', 
		])