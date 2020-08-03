from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from application.models import Users

class ProjectForm(FlaskForm):
    projectName = StringField('Project Name',
            validators = [
                DataRequired(),
                Length(min=1, max=100)
            ]
    )

    submit = SubmitField('Add Project')

class EpicForm(FlaskForm):
	epicName = StringField('Epic Name',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)

	submit = SubmitField('Add Epic')

class UStoryForm(FlaskForm):
	uStoryName = StringField('User Story Name',
			validators = [
				DataRequired(),
				Length(min=1, max=100)
			]
	)

	SubmitField = SubmitField('Add User Story')