import os
import unittest

from views import app, db
from config import basedir
from models import User

TEST_DB = 'test.db'

class Alltests(unittest.TestCase):

    # if a setUp() method is defined, the test runner will run that method
    # prior to each test.
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # if a tearDown() method is defined, the test runner will invoke that
    # method after each test.
    def tearDown(self):
        db.drop_all()

    def login(self, name, password):
        return self.app.post('/', data=dict(name=name, password=password),
                             follow_redirects=True)

    def logout(self):
        return self.app.get('logout/', follow_redirects=True)

    def create_user(self, name, email, password):
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

    def create_task(self):
        return self.app.post('add/', data=dict(name='Go buy milk',
                             due_date='04/21/2015',
                             priority='1',
                             posted_date='03/21/1015',
                             status='1'), follow_redirects=True)

    def test_users_can_add_tasks(self):
        self.create_user('testuser', 'testuser@email.com', 'python')
        self.login('testuser', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.create_task()
        self.assertIn('New entry was successfully posted. Thanks.',
                      response.data)

    def test_users_cannot_add_tasks_when_error(self):
        self.create_user('testuser', 'testuser@email.com', 'python')
        self.login('testuser', 'python')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.post('add/', data=dict(name='Go buy milk',
                                 due_date='',
                                 priority='1',
                                 posted_date='03/21/1015',
                                 status='1'), follow_redirects=True)
        self.assertIn('This field is required.', response.data)

    def test_users_can_update_tasks(self):
        self.create_user('testuser', 'testuser@email.com', 'python')
        self.login('testuser', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get("complete/1/", follow_redirects=True)
        self.assertIn('The task was marked as complete.', response.data)

    def test_users_can_delete_tasks(self):
        self.create_user('testuser', 'testuser@email.com', 'python')
        self.login('testuser', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        response = self.app.get("delete/1/", follow_redirects=True)
        self.assertIn('The task was deleted.', response.data)

    def test_users_cannot_complete_tasks_they_did_not_create_themselves(self):
        self.create_user('testuser', 'testuser@email.com', 'python')
        self.login('testuser', 'python')
        self.app.get('tasks/', follow_redirects=True)
        self.create_task()
        self.logout()
        self.create_user('testuser2', 'testuser2@email.com', 'python2')
        self.login('testuser2', 'python2')
        self.app.get('tasks/', follow_redirects=True)
        response = self.app.get("complete/1/", follow_redirects=True)
        self.assertNotIn('The task was marked as complete.', response.data)

if __name__ == "__main__":
    unittest.main()
