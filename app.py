from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:xxxx@192.168.1.174:3306/swan"

db=SQLAlchemy(app)

@app.route('/index')
def hello_world():

    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)