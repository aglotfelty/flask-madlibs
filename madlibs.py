from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_mad_lib_form():
    """Gets user's response regarding whether or not they want to play madlibs"""
 
    game_response = request.args.get("game-response")
    
    if game_response == "no":
        return render_template("goodbye.html")

    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    """Displays madlib game"""

    color = request.args.get("color")
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    classmates = request.args.getlist("classmate")
    length_of_classmates = len(classmates)
    # chosen_classmates = []
    

    print classmates
    return render_template("madlib.html", color=color, person=person, noun=noun, 
                            adjective=adjective, classmates=classmates, length=length_of_classmates)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
