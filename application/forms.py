from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, NumberRange
from application.models import Projects, UserStories

class ProjectForm(FlaskForm):
	projectName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )
	projectComplete = BooleanField('Completed?')
	submit = SubmitField('Add Project')

class UStoryForm(FlaskForm):
	uStoryName = StringField('User Story Name',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	projectID = IntegerField('Please Enter Project ID as a numerical value: ',
			validators = [
				DataRequired(),
				NumberRange(min=1, max=50)
			]
	)
	uStoryAsA = StringField('As a: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryIWant = StringField('I want: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryToSo = StringField('To/So: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryComplete = BooleanField('Completed?')
	SubmitField = SubmitField('Add User Story')

class UpdateUStoryForm(FlaskForm):
	uStoryName = StringField('User Story Name',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	projectID = IntegerField('Please Enter Project ID as a numerical value: ',
			validators = [
				DataRequired(),
				NumberRange(min=1, max=50)
			]
	)
	uStoryAsA = StringField('As a: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryIWant = StringField('I want: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryToSo = StringField('To/So: ',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)
	uStoryComplete = BooleanField('Completed?')
	SubmitField = SubmitField('Update User Story')

class UpdateProjectForm(FlaskForm):
	projectName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )
	projectComplete = BooleanField('Completed?')
	submit = SubmitField('Update Project')	