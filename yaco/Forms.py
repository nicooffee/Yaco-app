import sys
sys.path.append('class')
from wtforms import Form,StringField,validators
from Usuario import Usuario

class SearchForm(Form):
    busqueda = StringField('Busqueda', [validators.DataRequired()])


class UserForm(Form):
    usuario = StringField('Usuario', [validators.Length(min=5,max=20,message='Error de ingreso. Intente otra vez.')])
    contrasena = StringField('Contraseña',[validators.Length(min=4,max=32,message='Error de ingreso. Intente otra vez.')])
    connection = None
    
    def validate(self):
        if not Form.validate(self):
            return False
        usr = self.usuario.data
        psw = self.contrasena.data
        connection = self.connection
        if not Usuario.db_exists(usr,connection):
            self.contrasena.errors.append('Error de ingreso. Intente otra vez.')
            return False
        if Usuario.db_check_password(usr,psw,connection):
            return True
        self.contrasena.errors.append('Error de ingreso. Intente otra vez.')
        return False

class RevisionForm(Form):
    respuesta = StringField('Respuesta')
    flashcard = None
    def validate(self):
        if not Form.validate(self):
            return False
        if self.flashcard is not None:
            palabra = self.flashcard.get_palabra()
            if not palabra.contiene_def_str(self.respuesta.data,'es' if self.flashcard.get_tipo() == 'reco' else 'en'):
                self.respuesta.errors.append('Respuesta incorrecta')
                return False
            return True
        return False
