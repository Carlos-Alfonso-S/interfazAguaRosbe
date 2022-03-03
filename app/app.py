from flask import Flask, render_template, request
from app import config
from flask_mysqldb import MySQL

import app.forms

app=Flask(__name__, template_folder='./templates', static_folder='./static')

db=MySQL(app)

@app.route('/', methods = ['GET','POST'])
def index():
    #comment_form = forms.CommentForm(request.form)
    Usuario=False
    ID = 0
    while (not Usuario):
        try:
            cursor=db.connection.cursor()
            comment_form = forms.CommentForm(request.form)
            if request.method == 'POST' and comment_form.validate():
                busca= comment_form.iduser.data
                ##cursor.execute("SELECT Id_cliente, Nombre, Saldo FROM Clientes WHERE Id_cliente=('%s');"%busca)
                ##data=cursor.fetchall()
                return render_template('Index1.html', form= comment_form, data=busca)
            else:
                print('No esta registrado')    
                return render_template('inicioSesion.html', form= comment_form)
                
        except Exception as ex:
             return render_template('inicioSesion.html', form= comment_form)     

    return render_template('Index1.html') 



def inicializarApp(config):
    app.config.from_object(config)
    return app