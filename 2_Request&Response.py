from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return ("Hello world, my name is Diego and my IP is {}".format(user_ip))

if __name__ == '__main__':
    app.run(port=5000, debug=True)

#con user_ip = request.remote_addr conseguimos la ip del usuario que visita nuestro sitio o consulta nuestro sitio