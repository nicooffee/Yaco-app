import sys
import json
from datetime import datetime
from flask import (
    Blueprint, 
    render_template, 
    request,
    redirect,
    url_for,
    session,
    g,
    current_app,
    flash
)
sys.path.append('class/function')
from GetWord import get_word
from Desglose import desglose
from Forms import SearchForm

buscador_blueprint = Blueprint('buscar',__name__,template_folder='templates')

@buscador_blueprint.before_request
def before_request():
    if 'db' not in g:
        g.db = current_app.dbconnection
    if 'usr' not in session:
        return redirect(url_for('login.login'))

@buscador_blueprint.route("/buscar/<word>",methods=["GET","POST"])
def buscar(word):
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate():
        busqueda = form.busqueda.data
        return redirect(url_for('.buscar',word=busqueda))
    resultado=json.loads(desglose(get_word(word)))
    session['search'] = word
    session['search_res'] = resultado
    if len(resultado) == 0:
        flash('No se han encontado resultados.',category='warning')
    return render_template('buscador/buscador.html',
        date=datetime.now(),
        user=session['usr'],
        word=word,
        word_list=resultado
    )

