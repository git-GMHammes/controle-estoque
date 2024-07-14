from flask import Blueprint
from principal.view.main_view import main

router = Blueprint('router', __name__)

router.add_url_rule('/', view_func=main)
