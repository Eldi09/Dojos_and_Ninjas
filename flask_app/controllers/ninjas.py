from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/add_ninja')
def add_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojo']
    }
    Ninja.create_ninja(data)

    return redirect(f'/show_dojo/{data["dojos_id"]}')