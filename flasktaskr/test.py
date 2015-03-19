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

    def register(self, name, email, password, confirm):
        return self.app.post('register/', data=dict(name=name, email=email,
                             password=password, confirm=confirm),
                             follow_redirects=True)

    def test_user_setup(self):
        new_user = User("klabtani", "emailad@gmail.com", "kevinlabtani")
        db.session.add(new_user)
        db.session.commit()
        test = db.session.query(User).all()
        for t in test:
            t.name
        assert t.name == "klabtani"

    def test_form_is_present_on_login_page(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Please login to access your task list', response.data)

    def test_users_cannot_login_unless_registered(self):
        response = self.login('foo', 'bar')
        self.assertIn('Invalid username or password', response.data)

    def test_user_can_login(self):
        self.register('Michael', 'michael@email.com', 'python', 'python')
        response = self.login('Michael', 'python')
        self.assertIn('You are logged in.', response.data)

if __name__ == "__main__":
    unittest.main()
