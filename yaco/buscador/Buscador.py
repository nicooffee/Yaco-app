import sys
import json
from flask import (
    Blueprint, 
    render_template, 
    request,
    redirect,
    url_for,
    session
)
sys.path.append('class/function')
from GetWord import get_word
from Desglose import desglose
from Forms import SearchForm

buscador_blueprint = Blueprint('buscar',__name__,template_folder='templates')


@buscador_blueprint.route("/buscar/<word>",methods=["GET","POST"])
def buscar(word):
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate():
        busqueda = form.busqueda.data
        return redirect(url_for('buscar.buscar',word=busqueda))
    resultado=json.loads(desglose(get_word(word)))
    return render_template('buscador/buscador.html',user=session['usr'],word=word,word_list=resultado)