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
        app.config['WTF_CSRF_ENABLED']  =True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # if a tearDown() method is defined, the test runner will invoke that
    # method after each test.
    def tearDown(self):
        db.drop_all()


    def test_user_setup(self):
        new_user = User("klabtani", "emailad@gmail.com", "kevinlabtani")
        db.session.add(new_user)
        db.session.commit()

if __name__ == "__main__":
    unittest.main()
