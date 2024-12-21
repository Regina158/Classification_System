from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

# Inisialisasi Flask
app = Flask(__name__, template_folder='web')

# Mengonfigurasi Flask untuk menggunakan database MySQL di XAMPP
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/liver_cs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Mengonfigurasi Flask untuk melayani file statis dari folder 'Assets'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'Assets')

# Route untuk melayani file statis


@app.route('/Assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route untuk halaman utama (index)


@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman login


@app.route('/login')
def login():
    return render_template('login.html')


# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)
