from flask import Flask,session,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session,SqlAlchemySessionInterface
from principal.Principal import principal_blueprint
from login.Login import login_blueprint
from buscador.Buscador import buscador_blueprint
import sys
sys.path.append('class')
from Estudiante import Estudiante

app = Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nico:postgres@127.0.0.1:5432/sessions'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 2628000
app.config['SESSION_USE_SIGNER'] = True
app.secret_key = 'j22ea6juzrfFotTKYdSDjg'
app.config['DEBUG'] = True
#Blueprints####################################
app.register_blueprint(principal_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(buscador_blueprint)
###############################################
db = SQLAlchemy(app)

Session(app)
S = SqlAlchemySessionInterface(app, db, "sessions", "sess_")

@app.route('/logout-complete')
def logout_complete():
    S.sql_session_model.query.filter_by(session_id = 'session:'+request.cookies['session']).delete()
    S.db.session.commit()
    for key in list(session.keys()):
        session[key] = None
        session.pop(key)
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')