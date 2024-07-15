import os
from flask import Blueprint, render_template

# Caminho correto para a pasta de templates baseado na localização do módulo
template_dir = os.path.abspath(os.path.dirname(__file__))
template_folder_path = os.path.join(template_dir, '..', 'templates')

estoque_bp = Blueprint(
    'estoque_bp', __name__,
    template_folder=template_folder_path
)

@estoque_bp.route('/')
def stock():
    # Renderizar o template a partir do diretório especificado
    return render_template('stock_template.html')
