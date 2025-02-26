from flask import Flask , Blueprint ,render_template

main  = Blueprint('main',__name__)


"""

1) 'main' serves as the unique name for the blueprint.

__name__ provides Flask with the import path of the module, allowing it to correctly resolve resources associated with the blueprint.


2) 



"""
@main.route('/')

def index():
    return render_template('index.html') # used to loading the page of index.html from the folder named as templates which is the default folder in flask and here we are reffereing to the file named as index.html

