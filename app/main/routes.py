from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main_bp.route('/')
def index():
    return render_template('home.html', title="Home - Detección de Tomates")
