from flask import Flask,session,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session,SqlAlchemySessionInterface
from blueprint.principal.Principal import principal_blueprint
from blueprint.login.Login import login_blueprint
from blueprint.buscador.Buscador import buscador_blueprint
from blueprint.palabra_info.PalabraInfo import palabra_info_blueprint
from blueprint.revision_info.RevisionInfo import revision_info_blueprint
from blueprint.lista_palabra.ListaPalabra import lista_palabra_blueprint
import sys
import DatabaseData as dbdata
sys.path.append('class')
from database.Database import PSConnection
from Estudiante import Estudiante

app = Flask(__name__,static_url_path='/static')
app.dbconnection = PSConnection()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}:{}/{}".format(dbdata.user,dbdata.db_sess_pswd,dbdata.host,dbdata.port,dbdata.db_sess_name)
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
app.register_blueprint(palabra_info_blueprint)
app.register_blueprint(revision_info_blueprint)
app.register_blueprint(lista_palabra_blueprint)
###############################################


db = SQLAlchemy(app)

sess = Session(app)
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
    with app.app_context():
        app.run(host='0.0.0.0')