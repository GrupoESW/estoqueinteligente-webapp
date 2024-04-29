import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    api_url = os.environ.get('LETSENCRYPT_HOST').replace('webapp', 'apinode')
    title = "Login"
    return render_template('login.html', api_url=api_url,title=title)

@app.route('/login')
def login():
    api_url = os.environ.get('LETSENCRYPT_HOST').replace('webapp', 'apinode')
    title = "Login" 
    return render_template('login.html', api_url=api_url,title=title)

@app.route('/dashboard')
def dashboard():
    title = "Dashboard" 
    return render_template('dash.html',title=title)

@app.route('/estoque')
def estoque():
    api_url = os.environ.get('LETSENCRYPT_HOST').replace('webapp', 'apinode')
    title = "Estoque" 
    return render_template('estoque.html',api_url=api_url,title=title)

@app.route('/receitas')
def receitas():
    title = "Receitas" 
    return render_template('receitas.html',title=title)

@app.route('/sugestoes')
def sugestoes():
    title = "Sugestões" 
    return render_template('sugestoes.html',title=title)

@app.route('/config')
def config():
    title = "Configurações" 
    return render_template('configs.html',title=title)

if __name__ == '__main__':
    port_number = 80
    app.run(debug=True, host='0.0.0.0', port=port_number)


