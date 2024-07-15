import logging
from flask import Flask
from config.router import router
from estoque.views.stock_view import estoque_bp

# Configuração global do logger para gravar no diretório de logs
logging.basicConfig(level=logging.DEBUG, filename='/app/logs/app.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Registrar os Blueprints
app.register_blueprint(router)
app.register_blueprint(estoque_bp, url_prefix='/estoque')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
