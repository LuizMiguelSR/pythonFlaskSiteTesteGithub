from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina1', methods=['GET', 'POST'])
def pagina1():
    nome = request.form.get('nome')
    return render_template('pagina1.html', nome = nome)

if __name__ == "__main__":
    app.run()