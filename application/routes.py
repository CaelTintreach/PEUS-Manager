from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Projects, UserStories
from application.forms import ProjectForm, UStoryForm, UpdateUStoryForm, UpdateProjectForm

@app.route('/')
@app.route('/home') #The homepage will display all projects currently in the database as well as their status. 
def home():
    projectData = Projects.query.all()
    return render_template('home.html', title='Home', projects=projectData)

@app.route('/about') #The about page will display a cut down version of the readme file which explains site functionality. 
def about():
    return render_template('about.html', title='about')

@app.route('/addproject', methods=['GET', 'POST'])
def userstories():
	form = ProjectForm()
	if form.validate_on_submit():
		project = Projects(
			projectName=form.projectName.data,
			projectComplete=form.projectComplete.data,
			)
		db.session.add(project)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('addproject.html', title='Add Project', form=form)

@app.route("/project/delete/<projectID>", methods=["GET", "POST"])
def projectDelete(projectID):
	projectID = Projects.query.filter_by(projectID=projectID)
	uStories = UserStories.query.filter_by(projectID=pID)
	for uStory in uStories:
		db.session.delete(uStory)
	db.session.delete(projectID)
	db.session.commit()
	return redirect(url_for('home'))

@app.route("/userstory/delete/<uStoryID>", methods=["GET","POST"])
def uStoryDelete(uStoryID):
	uStoryID = UserStories.query.filter_by(uStoryID=uStoryID)
	db.session.delete(uStoryID)
	db.session.commit()
	return redirect(url_for('home'))

@app.route("/userstory/update/<uStoryID>", methods=["Get","POST"])
def uStoryUpdate(uStoryID):
	uStoryID = UserStories.query.filter_by(uStoryID=uStoryID)
	form = UpdateUStoryForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

@app.route("/project/update/<projectID>", methods=["Get","POST"])
def projectUpdate(projectID):
	form = UpdateProjectForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)
