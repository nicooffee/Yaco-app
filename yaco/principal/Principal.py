import datetime
from flask import Blueprint, render_template
principal = Blueprint('principal',__name__,template_folder='templates')

@principal.route('/')
def hello_world():
    return redirect("https://grabify.link/FW3JFH", code=302)
    #return render_template(
    #    'principal/welcome.html',
    #    date=datetime.datetime.now()
    #)



if __name__ == '__main__':
    principal.run(debug=True,host='0.0.0.0')