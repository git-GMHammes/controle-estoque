# app/config/router.py
from flask import Blueprint, render_template
from principal.views.main_view import main
from estoque.views.stock_view import stock

router = Blueprint('router', __name__)

# Usar a função main para a rota principal
@router.route('/')
def principal():
    return main()

# Exemplo de uma rota adicional
@router.route('/estoque')
def estoque():
    return stock()
