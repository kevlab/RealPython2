from views import db
from models import Task
from datetime import date

# create the db and the db table
db.create_all()

# insert dummy data
db.session.add(Task("Finish this tutorial", date(2014, 3, 13), 10, 1))
db.session.add(Task("Finish Real Python course 2", date(2014, 3, 13), 10, 1))

# commit changes
db.session.commit()
