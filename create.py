from application import db
from application.models import Projects, Epics

db.drop_all()
db.create_all()