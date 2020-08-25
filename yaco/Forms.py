import sys
sys.path.append('class')
from wtforms import Form,StringField,validators
from Usuario import Usuario

class SearchForm(Form):
    busqueda = StringField('Busqueda', [validators.DataRequired()])


class UserForm(Form):
    usuario = StringField('Usuario', [validators.Length(min=5,max=20,message='Nombre de usuario debe ser entre 5 y 20 caracteres.')])
    contrasena = StringField('Contraseña',[validators.Length(min=4,max=32,message='Contraseña debe ser entre 8 y 32 caracteres.')])

    def validate_usuario(self,field):
        if not Usuario.db_exists(field.data):
            raise validators.ValidationError("Usuario no encontrado.")
    
    def validate(self):
        if not Form.validate(self):
            return False
        usr = self.usuario.data
        psw = self.contrasena.data
        if Usuario.db_check_password(usr,psw):
            return True
        self.contrasena.errors.append('Contraseña incorrecta. Intente otra vez.')
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
