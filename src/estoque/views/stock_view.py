from flask import Blueprint, render_template

estoque_bp = Blueprint(
    'estoque_bp', __name__,
    template_folder='templates'
)

@estoque_bp.route('/')
def stock():
    return render_template('stock_template.html')
