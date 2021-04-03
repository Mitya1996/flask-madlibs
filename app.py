from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    names = [a.story_name for a in stories]
    return render_template('home.html', names=names)

@app.route('/questions')
def questions():
    #get correct story based on name
    story_name = request.args.get('stories-choice')
    story = [s for s in stories if s.story_name == story_name][0] #getstory from stories array

    blanks = story.prompts
    return render_template('questions.html', story_name=story_name, blanks=blanks)

@app.route('/story/<story_name>')
def madlib(story_name):
    story = [s for s in stories if s.story_name == story_name][0] #getstory from stories array

    madlib = story.generate(request.args)

    return render_template('story.html', madlib = madlib)