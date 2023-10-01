import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    api_url = os.environ.get('LETSENCRYPT_HOST').replace('webapp', 'api')
    return render_template('login.html', api_url=api_url)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/receitas')
def receitas():
    return render_template('receitas.html')

@app.route('/sugestoes')
def sugestoes():
    return render_template('sugestoes.html')

@app.route('/alertas')
def alertas():
    return render_template('alertas.html')

@app.route('/config')
def config():
    return render_template('configs.html')

if __name__ == '__main__':
    port_number = 80
    app.run(debug=True, host='0.0.0.0', port=port_number)
