from flask import Flask, render_template, redirect
from .config import Config
from app.shipping_form import Shipping_Form

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
    return "Package Tracker"


@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = Shipping_Form()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('shipping_request.html', form=form)
 