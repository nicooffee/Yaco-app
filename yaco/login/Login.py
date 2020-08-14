import sys
sys.path.append('class')
from Usuario import Usuario
from flask import (
    Blueprint, 
    render_template, 
    request,
    redirect,
    url_for,
    session
)
login_blueprint = Blueprint('login',__name__,template_folder='templates')

@login_blueprint.route('/login', methods =["GET","POST"])
def login():
    if request.method == 'POST':
        session.pop('usr',None)
        user_data = {'usr': request.form['usuario'], 'psw': request.form['contrasena']}
        existe = Usuario.db_exists(user_data['usr'])
        if existe and Usuario.db_check_password(user_data['usr'],user_data['psw']):
            session['usr'] = user_data['usr']
            return redirect(url_for('principal.dashboard'))
        return render_template('login/login.html') 
    else:
        return render_template('login/login.html')

@login_blueprint.route('/logout')
def logout():
    session.pop('usr',None)
    return redirect(url_for('login.login'))