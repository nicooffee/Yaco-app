from flask import Flask,session,redirect,url_for,g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session,SqlAlchemySessionInterface
from principal.Principal import principal_blueprint
from login.Login import login_blueprint
import sys
sys.path.append('class')
from Estudiante import Estudiante


app = Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nico:postgres@127.0.0.1:5432/sessions'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.secret_key = '1234'
app.config['DEBUG'] = True
#Blueprints####################################
app.register_blueprint(principal_blueprint)
app.register_blueprint(login_blueprint)
###############################################

db = SQLAlchemy(app)
Session(app)
SqlAlchemySessionInterface(app, db, "sessions", "sess_")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')