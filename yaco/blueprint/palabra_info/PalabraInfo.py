import sys
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    request,
    url_for,
    session,
    current_app,
    flash
)
sys.path.append('class')
from database.Database import PSConnection
from Palabra import Palabra
from Forms import SearchForm

palabra_info_blueprint = Blueprint('palabrainfo',__name__,template_folder='templates')

@palabra_info_blueprint.before_request
def palabrainfo_before_request():
    if 'db' not in g:
        g.db = current_app.dbconnection
    if 'usr' not in session:
        return redirect(url_for('login.login'))
    if 'search' in session:
        g.busqueda = session['search']
    g.last_search = session['search_res'] if 'search_res' in session else []



@palabra_info_blueprint.route('/palabra/<id>',methods = ["GET","POST"])
def palabra_info(id):
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate():
        busqueda = form.busqueda.data
        return redirect(url_for('buscar.buscar',word=busqueda))
    else:
        user = session['usr']
        g.word = user.get_palabra(id)
        g.added = True
        if g.word is None:
            g.added = False
            word_dict = get_word(g.last_search,id)
            g.word = Palabra.from_dict(word_dict,user.get_id())
            if g.word is not None:
                session['w_actual'] = word_dict
            else:
                return redirect(url_for('principal.dashboard'))
        return render_template('palabrainfo/palabra-info.html',
            user = user,
            date = datetime.now()
        )

@palabra_info_blueprint.route('/agregar_actual')
def agregar_actual():
    if 'w_actual' in session:
        w_dict = session.pop('w_actual')
        user = session['usr']
        w = user.agregar_palabra(g.db,w_dict)
        flash('Palabra agregada exitósamente','primary')
        return redirect(url_for('.palabra_info',id=w.get_id()))
    else:
        return redirect(url_for('principal.dashboard'))

@palabra_info_blueprint.route('/eliminar/<id>')
def eliminar_actual(id):
    if id != '':
        user = session['usr']
        w = user.eliminar_palabra(g.db,id)
        if w is None:
            flash('La palabra no se ha eliminado puesto que no se ha encontrado en las palabras aprendidas')
        else:
            flash('Palabra eliminada exitósamente.',category='warning')
    if 'search' in session and session['search']!='':
        return redirect(url_for('buscar.buscar',word=session['search']))
    else:
        if 'last_page' in session:
            return redirect(url_for(session['last_page']))
        else:
            return redirect(url_for('principal.dashboard'))

def get_word(L,id):
    for w in L:
        if w['id'] == id:
            return w
    return None