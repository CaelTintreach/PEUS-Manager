from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Projects 
from application.forms import ProjectForm, EpicForm, UStoryForm

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
		project = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data,
			)

		db.session.add(project)
		db.session.commit()

		return redirect(url_for('home'))

@app.route("/epic/delete", methods=["GET", "POST"])
def epic_delete():
		epic = projects.id
		uStories = Epics.query.filter_by(epicID=epic)
		for epic in epics:
				db.session.delete(post)
				db.session.commit()
		return redirect(url_for('home'))

@app.route('/post', methods=['GET', 'POST'])
def post():
	form = PostForm()
	if form.validate_on_submit():
		postData = Posts(
			title=form.title.data,
			content=form.content.data,
			author=current_user
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		print(form.errors)
	return render_template('post.html', title='Post', form=form)