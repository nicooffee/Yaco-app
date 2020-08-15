from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    url_for,
    session
)
import datetime
principal_blueprint = Blueprint('principal',__name__,template_folder='templates')

@principal_blueprint.route('/')
def dashboard():
    if 'usr' not in session:
        return redirect(url_for('login.login'))
    return render_template(
        'principal/welcome.html',
        date=datetime.datetime.now()
    )



if __name__ == '__main__':
    principal.run(debug=True,host='0.0.0.0')