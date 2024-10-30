import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Login"
    return render_template('login.html', api_url="http://" + api_url + "/api",title=title)

@app.route('/login')
def login():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Login" 
    return render_template('login.html', api_url="http://" + api_url + "/api",title=title)

@app.route('/dashboard')
def dashboard():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Dashboard" 
    return render_template('dash.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/estoque')
def estoque():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Estoque"
    return render_template('estoque.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/receitas')
def receitas():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Receitas"
    return render_template('receitas.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/sugestoes')
def sugestoes():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Sugestões"
    return render_template('sugestoes.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/cadastro')
def cadastro():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Cadastro"
    return render_template('cadastro.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/logout')
def logout():
    api_url = os.environ.get('VIRTUAL_HOST')
    title = "Logout"
    return render_template('logout.html',api_url="http://" + api_url + "/api",title=title)

@app.route('/config')
def config():
    title = "Configurações"
    return render_template('configs.html',title=title)

if __name__ == '__main__':
    port_number = 80
    app.run(debug=True, host='0.0.0.0', port=port_number)


