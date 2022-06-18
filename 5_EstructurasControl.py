from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar Cafe', 'Arreglar algo', 'Limpiar la casa']

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response



@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos
    }
    return render_template('5_hello.html', **context)


if __name__ == '__main__':
    app.run(port=5000,debug=True)

#si encontramos la ip del usuario, rendereamos un html <h1>, sino lo encontramos, rendereamos un link con <a>

#la variable url_for nos permite encontrar la ruta especifica solo con colocar el nombre de esa ruta
#por ejemplo, ponemos url_for('index') y nos referimos a la ruta raiz '/' y al metodo index dentro de la ruta

#para evitar llenarnos de variables asi : return render_template('5_hello.html', user_ip=user_ip, todos = todos, ....) lo que hacemos es crear un diccionario con las claves como nombre de las variables en los valores son las variables como tal -> este diccionario se llama context.

#si context se pasa asi nomas : return render_template('5_hello.html', context=context) lo que pasaría es que tendriamos que en colocar context.user_ip o context.todos en cada etiqueta html, para evitar eso hacemos el **context y de esa forma expandimos un diccionario