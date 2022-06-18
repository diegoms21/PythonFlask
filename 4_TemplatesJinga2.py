from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response



@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return render_template('4_hello.html', user_ip=user_ip)


if __name__ == '__main__':
    app.run(port=5000,debug=True)

#Tenemos que crear la ruta por defecto de "templates" y flask jalará de ahí todos los archivos html

#Para mandarle una variable al html renderizado desde templates, tenemos que enviarle por render_template y en el html invocarlo con doble lave -> {{user_ip}}