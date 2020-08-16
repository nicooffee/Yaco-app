import sys
sys.path.append('class')
from Usuario import Usuario
from Estudiante import Estudiante
from Forms import UserForm
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
    session.pop('usr',None)
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        usr = form.usuario.data
        session['usr'] = Estudiante.from_db(usr)
        return redirect(url_for('principal.dashboard'))
    else:
        return render_template('login/login.html')

@login_blueprint.route('/logout')
def logout():
    return redirect(url_for('logout_complete'))