from flask import Flask, render_template
from flask import request
from flask_mysqldb import MySQL

import forms


app=Flask(__name__, template_folder='./templates', static_folder='./templates/static')

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
                cursor.execute("SELECT Id_cliente, Nombre, Saldo FROM Clientes WHERE Id_cliente=('%s');"%busca)
                data=cursor.fetchall()
                return render_template('Index1.html', form= comment_form, data=data)
            else:
                print('No esta registrado')    
                return render_template('inicioSesion.html', form= comment_form)
                
        except Exception as ex:
             return render_template('inicioSesion.html', form= comment_form)     

    return render_template('Index1.html') 






def restaBD(opcion1):
    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM Clientes WHERE Id_cliente=('%s');"% opcion1)
    res=cursor.fetchone()
    for saldo in res:
        res[3]
        sal=res[3]
        if sal==0.00:
            print("No tiene saldo")
        else:
            cursor.execute("UPDATE Clientes SET Saldo = (Saldo - 3) WHERE  Id_cliente =%s"%opcion1)
            db.commit()
            print ("Llenando Botella de 1 litro")
            salir = True
###Seleccion del producto
def menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elegie una opcion: "))
            correcto=True
        except ValueError:
            print('Error, no existe esa opcion')
     
    return num



##
##@app.route('/ejemplo01')
##def basedatosEjemplo():
  ##  data={
    ##    'canal':'Goku',
      ##  'Anime': ['Naruto', 'Dragon Ball', 'Boku no hero','Pokemon']
    ##}
    ##return render_template('ejemplo01.html', data=data)

#@app.route('/usuarios')
#def listadoUsuarios():
#    try:
#        cursor=db.connection.cursor()
 #       sql = "SELECT Id_cliente, Nombre, Saldo FROM Clientes"
 #       cursor.execute(sql)
  #      data = cursor.fetchall()
   #     return render_template('inicioSesion.html', data=data)
   # except Exception as ex:
   #     return "Error"


#@app.route('/usuario')
#def formulario():
    #try:
 #       comment_form = forms.CommentForm()
        ##cursor=db.connection.cursor()
       ## busca= request.args.get('idusuario')
        ##if(busca != ''):
        ##sql= "SELECT Id_cliente, Nombre, Saldo FROM Clientes WHERE Id_cliente=('%s');"
        ##cursor.execute(sql,busca)
       ## data = cursor.fetchall()
  #      return render_template('inicioSesion.html', form= comment_form)
        ##else:
            ##return render_template('inicioSesion.html')
    #except Exception as ex:
     #   return 'Error'


    



def inicializarApp(config):
    app.config.from_object(config)
    return app