import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Projects, UserStories
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test project
        testProject = Projects(projectName="testProject", projectComplete="True")

        # create test user story
        testUS = UserStories(first_name="test", last_name="user")

        # save users to database
        db.session.add(testProject)
        db.session.add(testUS)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):
    def test_add_new_post(self):
        """
        Test that when I add a new post, I am redirected to the homepage with the new post visible
        """
        with self.client:
            self.client.post(
                url_for('login'), 
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
            response = self.client.post(
                url_for('post'),
                data=dict(
                    title="Test title",
                    content="Test content"),
                follow_redirects=True )
            self.assertIn(b'Test title', response.data)

class TestPostAccess(TestBase):
    def test_access_post_page(self):
        #Test that determines what happens if you try to access the post page while logged out
        with self.client:
            response = self.client.post(url_for('post'),
                follow_redirects=True)
            self.assertIn(b'Register', response.data)

class TestAboutPage(TestBase):
    def test_access_about_page(self):
        #Test the about page can be accessed
        response = self.client.get(url_for('about'))
        self.assertIn(b'About Page', response.data)

class TestAccountDelete(TestBase):
    def test_delete_account(self):
        self.client.post(
                url_for('login'),
                data=dict(
                    email='admin@admin.com',
                    password='admin2016'),
                follow_redirects=True)
        self.client.post(url_for('account'),
                follow_redirects=True)
        self.client.post(url_for('account_delete'),
                follow_redirects=True)
        response = self.client.get(url_for('login'))
        self.assertIn(b'Login',response.data)