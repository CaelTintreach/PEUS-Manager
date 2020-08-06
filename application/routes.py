from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Projects, UserStories
from application.forms import ProjectForm, UStoryForm, UpdateUStoryForm, UpdateProjectForm

@app.route('/about') #The about page will display a cut down version of the readme file which explains site functionality. 
def about():
    return render_template('about.html', title='About')

@app.route('/addproject', methods=['GET', 'POST'])
def addproject():
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

@app.route('/adduserstory', methods=['GET', 'POST'])
def adduserstory():
	form = UStoryForm()
	if form.validate_on_submit():
		uStory = UserStories(
			uStoryName=form.uStoryName.data,
			projectID=form.projectID.data,
			uStoryAsA=form.uStoryAsA.data,
			uStoryIWant=form.uStoryIWant.data,
			uStoryToSo=form.uStoryToSo.data,
			uStoryComplete=form.uStoryComplete.data
		)
		db.session.add(uStory)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('adduserstory.html', title='Add User Story', form=form)

@app.route('/')
@app.route('/home') #The homepage will display all projects currently in the database as well as their status. 
def home():
    projectData = Projects.query.all()
    return render_template('home.html', title='Home', Projects=projectData)

@app.route("/updateproject/<projectID>", methods=["Get","POST"])
def projectUpdate(projectID):
	projectID = UserStories.query.filter_by(projectID=id)
	form = ProjectForm()
	if form.validate_on_submit():
		Projects.projectName = form.projectName.data
		Projects.projectComplete = form.projectComplete.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.projectName.data = Projects.projectName
		form.projectComplete.data = Projects.projectComplete
	return render_template('account.html', title='Account', form=UpdateUStoryForm)
'''
@app.route("/updateuserstory/<uStoryID>", methods=["Get","POST"])
def uStoryUpdate(uStoryID):
	uStoryID = UserStories.query.filter_by(uStoryID=id)
	form = UpdateUStoryForm()
	if form.validate_on_submit():
		current_user.first_name = form.projectName.data
		current_user.last_name = form.projectComplete.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.projectName.data = current_user.projectName
		form.projectComplete.data = current_user.projectComplete
	return render_template('account.html', title='Account', form=UpdateUStoryForm)
'''
@app.route("/project/delete/<projectID>", methods=["GET", "POST"])
def projectDelete(projectID):
	projectID = Projects.query.filter_by(projectID=id)
	uStories = UserStories.query.filter_by(projectID=pID)
	for uStory in uStories:
		db.session.delete(uStory)
	db.session.delete(projectID)
	db.session.commit()
	return redirect(url_for('home'))

@app.route("/userstory/delete/<uStoryID>", methods=["GET","POST"])
def uStoryDelete(uStoryID):
	uStoryID = UserStories.query.filter_by(uStoryID=id)
	db.session.delete(uStoryID)
	db.session.commit()
	return redirect(url_for('home'))

@app.route('/viewuserstory')
def viewuserstory():
    UStoryData = UserStories.query.all()
    return render_template('home.html', title='Home', UserStories=UStoryData)