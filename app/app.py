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

if __name__ == '__main__':
    app.run(debug=True)