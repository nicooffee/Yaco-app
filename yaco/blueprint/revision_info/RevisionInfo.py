import sys
from datetime import datetime
from Forms import RevisionForm
from blueprint.revision_info.FlashcardDict import FlashcardDict
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
from database.Database import PSConnection

revision_info_blueprint = Blueprint('revisioninfo',__name__,template_folder='templates')


@revision_info_blueprint.before_request
def revisioninfo_before_request():
    if 'usr' not in session:
        return redirect(url_for('login.login'))
    if 'lastrev' not in session:
        session['lastrev'] = []

@revision_info_blueprint.route('/revision-sumario')
def revision_sumario():
    flash_list = session['usr'].list_review_disponible(fecha=datetime.now())
    session['review_disponible'] = FlashcardDict(flash_list)
    return render_template('revisioninfo/revision-sumario.html',user = session['usr'], date = datetime.now(), rev_list = session['lastrev'])


@revision_info_blueprint.route('/revisiones')
def get_dict_revision():
    try:
        current = session['review_disponible'].current()
        session['lastrev'] = []
    except StopIteration:
        return redirect(url_for('.revision_sumario'))
    return redirect(url_for('.sesion_revision',fid=current))

@revision_info_blueprint.route('/revisiones/<fid>', methods =["GET","POST"])
def sesion_revision(fid):
    try:
        f_dict = session['review_disponible']
        if request.method == 'POST':
            form = RevisionForm(request.form)
            form.flashcard = f_dict.get_flashcard(fid)
            fid_next = f_dict.get_next(fid)
            f_dict.set_last_res(fid,form.respuesta.data)
            if form.validate():
                data_aux = f_dict.pop(fid)
                f_aux = data_aux['flashcard']
                r_aux = f_aux.completar_revision(not data_aux['eq_prev'])                
                session['lastrev'].append({'id':f_aux.get_palabra().get_id(),'correcta':not data_aux['eq_prev'],'palabra':f_aux.get_palabra().get_definicion_principal('en').get_definicion(),'tipo':f_aux.get_tipo()})
                f_aux.add_data()
                r_aux.add_data()
                psc = PSConnection()
                psql_query = """INSERT INTO PUBLIC."FLASHCARD_REVISION" (rev_id,fla_id,rev_fla_fecha) 
                                VALUES (%s,%s,%s) 
                                ON CONFLICT ON CONSTRAINT "PK_FLA_REV" DO NOTHING"""
                data = (r_aux.get_id(),f_aux.get_id(),r_aux.get_fecha())
                psc.query(psql_query,data)
            else:
                f_dict.set_eq_prev(fid,True)
                return redirect(url_for('.sesion_revision_error',fid = fid))
            if fid_next is None:
                flash('¡Sesión de revisiones terminada!',category='success')
                return redirect(url_for('.revision_sumario'))
            else:
                return redirect(url_for('.sesion_revision',fid=fid_next))
        else:
            return render_template('revisioninfo/revision.html',flashcard = f_dict.get_flashcard(fid),rev_cant=len(f_dict))
    except KeyError as e :
        print('error', e)
        return redirect(url_for('.revision_sumario'))

@revision_info_blueprint.route('/revisiones/<fid>/error', methods =["GET","POST"])
def sesion_revision_error(fid):
    f_dict = session['review_disponible']
    if request.method == 'POST':
        f_dict.repos()
        fid_next = f_dict.get_first()
        if fid_next is None:
            flash('¡Sesión de revisiones terminada!',category='success')
            return redirect(url_for('.revision_sumario'))
        else:
            return redirect(url_for('.sesion_revision',fid=fid_next))
    else:
        return render_template('revisioninfo/revision-error.html',error=f_dict.get_last_res(fid),flashcard = f_dict.get_flashcard(fid),next = f_dict.get_next(fid),rev_cant=len(f_dict))