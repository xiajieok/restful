from flask_script import Manager
from app import app,db
from models import User
manager = Manager(app)
@manager.command
def save():
    # user = User(1,'tom')
    # user.save()
    # pass
    user = User(2,'cat')
    db.session.add(user)
    db.session.commit()

@manager.command
def query_all():
    users = User.query.all()
    # for u in users:
    #     print(u)
    # pass
    for u in users:
        print(u)

if __name__ == '__main__':
    manager.run()