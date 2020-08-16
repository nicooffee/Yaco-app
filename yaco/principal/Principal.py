import datetime
from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    request,
    url_for,
    session
)
from Forms import SearchForm


principal_blueprint = Blueprint('principal',__name__,template_folder='templates')

@principal_blueprint.route('/',methods =["GET","POST"])
def dashboard():
    form = SearchForm(request.form)
    if request.method == "POST" and form.validate():
        busqueda = form.busqueda.data
        return redirect(url_for('buscar.buscar',word=busqueda))
    if 'usr' not in session:
        return redirect(url_for('login.login'))
    return render_template(
        'principal/welcome.html',
        user=session['usr'],
        date=datetime.datetime.now(),
        form = form
    )



if __name__ == '__main__':
    principal.run(debug=True,host='0.0.0.0')