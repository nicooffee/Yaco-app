from wtforms import Form,StringField,validators

class SearchForm(Form):
    busqueda = StringField('Busqueda', [validators.DataRequired()])
