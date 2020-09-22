import sys
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    current_app,
    request,
    url_for,
    session,
    flash
)
from Forms import SearchForm
sys.path.append('class')
from database.Database import PSConnection

lista_palabra_blueprint = Blueprint('listapalabra',__name__,template_folder='templates')

@lista_palabra_blueprint.before_request
def listapalabra_before_request():
    session['search'] = ''
    session['last_page'] = 'listapalabra.listar_palabras'
    if 'db' not in g:
        g.db = current_app.dbconnection
    if 'usr' not in session:
        return redirect(url_for('login.login'))

@lista_palabra_blueprint.route('/palabras',methods=['GET','POST'])
def listar_palabras():
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate():
        busqueda = form.busqueda.data
        return redirect(url_for('buscar.buscar',word=busqueda))
    user = session['usr']
    return render_template('listapalabra/lista-palabra.html',user = user, date = datetime.now(),word_list=user.get_palabra_iter())