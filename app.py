from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    blanks = story.prompts
    return render_template('questions.html', blanks=blanks)

@app.route('/story')
def madlib():

    madlib = story.generate(request.args)

    return render_template('story.html', madlib = madlib)