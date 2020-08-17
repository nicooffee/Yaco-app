from datetime import datetime
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
    user = session.get('usr')
    srslvl = [user.cant_flashcard(1)+user.cant_flashcard(2)+user.cant_flashcard(3)+user.cant_flashcard(4)+user.cant_flashcard(5),user.cant_flashcard(6),user.cant_flashcard(7),user.cant_flashcard(8)]
    return render_template(
        'principal/welcome.html',
        user=user,
        date=datetime.now(),
        srslvl=srslvl,
        form = form
    )



if __name__ == '__main__':
    principal.run(debug=True,host='0.0.0.0')