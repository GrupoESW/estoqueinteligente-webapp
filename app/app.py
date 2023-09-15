import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    api_url = os.environ.get('LETSENCRYPT_HOST').replace('webapp', 'api')
    return render_template('index.html', api_url=api_url)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

if __name__ == '__main__':
    port_number = 80
    app.run(debug=True, host='0.0.0.0', port=port_number)