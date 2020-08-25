import sys
from datetime import datetime
from Forms import RevisionForm
from flask import (
    Blueprint,
    render_template,
    g,
    redirect,
    request,
    url_for,
    session,
    flash
)
sys.path.append('class')

revision_info_blueprint = Blueprint('revisioninfo',__name__,template_folder='templates')


@revision_info_blueprint.before_request
def revisioninfo_before_request():
    if 'usr' not in session:
        return redirect(url_for('login.login'))
    if 'lastrev' not in session:
        session['lastrev'] = []


@revision_info_blueprint.route('/revision-sumario')
def revision_sumario():
    session['review_disponible'] = session['usr'].dict_review_disponible()
    return render_template('revisioninfo/revision-sumario.html',user = session['usr'], date = datetime.now(), rev_list = session['lastrev'])


@revision_info_blueprint.route('/revisiones')
def get_dict_revision():
    try:
        current = next(iter(session['review_disponible']))
    except StopIteration:
        return redirect(url_for('.revision_sumario'))
    return redirect(url_for('.sesion_revision',fid=current))

@revision_info_blueprint.route('/revisiones/<fid>', methods =["GET","POST"])
def sesion_revision(fid):
    try:
        f_dict = session['review_disponible']
        if request.method == 'POST':
            form = RevisionForm(request.form)
            form.flashcard = f_dict[fid]['flashcard']
            if form.validate():
                pass
            else:
                pass
            if f_dict[fid]['next'] is None:
                return redirect(url_for('.revision_sumario'))
            else:
                return redirect(url_for('.sesion_revision',fid=f_dict[fid]['next']))
        else:
            return render_template('revisioninfo/revision.html',flashcard = f_dict[fid]['flashcard'],next = f_dict[fid]['next'])
    except KeyError:
        return redirect(url_for('.revision_sumario'))