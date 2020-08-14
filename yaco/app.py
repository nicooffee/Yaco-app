from flask import Flask,session,redirect,url_for,g
from principal.Principal import principal_blueprint
from login.Login import login_blueprint
import sys
sys.path.append('class')
from Estudiante import Estudiante


app = Flask(__name__,static_url_path='/static')
app.secret_key = '1234'
app.config['DEBUG'] = True
app.register_blueprint(principal_blueprint)
app.register_blueprint(login_blueprint)

@app.before_request
def before_request():
    g.user = None
    if 'usr' in session:
        E = Estudiante.from_db(session['usr'])
        g.user = E

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')