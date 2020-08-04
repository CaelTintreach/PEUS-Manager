from application import db

class Projects(db.model):
	projectID = db.Column(db.Integer, primary_key=True)
	projectName = db.Column(db.String(100), nullable=False, unique=True)
	projectComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)
	ustories = db.relationship('User Stories', backref='uStoryBR', lazy=True)

	def __repr__(self):
		return ''.join([
			'Project ID: ', self.projectID, '\r\n',
			'Project Name: ', self.projectName, '\r\n'
		])

class UserStories(db.model):
	uStoryID = db.Column(db.Integer, primary_key=True)
	pID = db.Column(db.Integer, db.ForeignKey('Projects.projectID'), nullable=False)
	uStoryName = db.Column(db.String(100), nullable=False, unique=True)
	uStoryComplete = db.Column(db.Boolean, nullable=False, unique=False, default=False)
	uStoryAsA = db.Column(db.String(500), nullable=False, unique=True)
	uStoryIWant = db.Column(db.String(500), nullable=False, unique=True)
	uStoryToSo = db.Column(db.String(500), nullable=False, unique=True)

	def __repr__(self):
		return ''.join([
			'User Story ID: ', self.ustoryID, '\r\n',
			'User Story Name: ', self.ustoryName, '\r\n', 
			'As A: ', self.ustoryAsA, '\r\n',
			'I Want: ', self.ustoryIWant, '\r\n',
			'To/So: ',  self.ustoryToSo, '\r\n'
		])