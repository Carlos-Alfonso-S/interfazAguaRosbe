from email import message
from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import validators


class CommentForm(Form):
    iduser= IntegerField('Id de usuario:',
    [
        validators.length(min=1, max=10, message='Ingrese un Id valido!.'),
        validators.DataRequired(message = 'El Id es requerido!.')
    ]
    )
    opcion1= IntegerField('Elige una opcion:')
