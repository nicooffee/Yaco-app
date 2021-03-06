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
    session,
    current_app,
    g,
    flash
)
login_blueprint = Blueprint('login',__name__,template_folder='templates')

@login_blueprint.before_request
def before_request():
    if 'db' not in g:
        g.db = current_app.dbconnection

@login_blueprint.route('/login', methods =["GET","POST"])
def login():    
    session.pop('usr',None)
    form = UserForm(request.form)
    form.connection = g.db
    if request.method == 'POST' and form.validate():
        usr = form.usuario.data
        session['usr'] = Estudiante.from_db(g.db,usr)
        flash('Ha entrado a la plataforma exitósamente',category='success')
        return redirect(url_for('principal.dashboard'))
    else:
        if request.method == 'POST':
            flash('Error de ingreso. Intente otra vez.',category='danger')
        return render_template('login/login.html')

@login_blueprint.route('/logout')
def logout():
    return redirect(url_for('logout_complete'))