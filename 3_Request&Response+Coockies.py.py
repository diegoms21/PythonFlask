from flask import Flask, request, make_response, redirect

#le pasamos el nombre de la aplicación, que en el archivo se llama main.py
app = Flask(__name__)

@app.route('/')
def index():
    #con request.remote_addr podemos obtener la ip de la persona que visita o consutla nuestro sitio
    user_ip = request.remote_addr

    #para crear una respuesta usamos make_response, la respuesta la guardamos en una variable.
    response = make_response(redirect('/hello'))

    #le pedimos que ponga una cookie igual a la ip del usuario
    response.set_cookie('user_ip', user_ip)

    return response


#cuando el buscador haga una consulta a nuestro servidor, va a llegar a la ruta raiz y esta regresará la función con el mensaje 'Hello Diego'
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return 'Hello Diego, la IP del visitante es {}'.format(user_ip)

@app.route('/test')
def test():
    return '<h1>hola</h1>'

if __name__ == '__main__':
    app.run(port=5000,debug=True)

#En una ruta donde detectaremos la ip, lo guardaremos en una cookie, lo redirijiremos al usuario a la hello desde la ruta inicial index