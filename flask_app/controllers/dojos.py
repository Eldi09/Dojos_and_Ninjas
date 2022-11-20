from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def dojos():
    result = Dojo.get_all_dojos()
    return render_template('dojo.html', all_dojos = result)

@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/show_dojo/<int:id>')
def show_dojo(id):
    results = Dojo.get_all_dojos()
    data = {
        'id': id
    }
    for dojo in results:
        if dojo.id == id:
            the_dojo = dojo
    ninjas = Dojo.ninjas_of_dojo(data)
    return render_template('dojo_show.html', dojo = the_dojo, ninjas = ninjas)
