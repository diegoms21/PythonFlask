from flask import Flask, request

#le pasamos el nombre de la aplicación, que en el archivo se llama main.py
app = Flask(__name__)

#cuando el buscador haga una consulta a nuestro servidor, va a llegar a la ruta raiz y esta regresará la función con el mensaje 'Hello Diego'
@app.route('/')
def hello():
    #con request.remote_addr podemos obtener la ip de la persona que visita o consutla nuestro sitio
    user_ip = request.remote_addr
    return 'Hello Diego, la IP del visitante es {}'.format(user_ip)