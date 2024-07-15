from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config.router import router

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pass123@mysql-db/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Registrar o Blueprint das rotas
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
