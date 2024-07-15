from flask import Blueprint
from principal.view.main_view import main
from estoque.view.stock_view import stock
# from produto.views.product_view import produto_bp
# from usuario.views.user_view import usuario_bp

router = Blueprint('router', __name__)

router.add_url_rule('/', view_func=main)
router.add_url_rule('/estoque', view_func=stock)


# router.register_blueprint(main_bp, url_prefix='/')
# router.register_blueprint(estoque_bp, url_prefix='/estoque')
# router.register_blueprint(produto_bp, url_prefix='/produto')
# router.register_blueprint(usuario_bp, url_prefix='/usuario')

