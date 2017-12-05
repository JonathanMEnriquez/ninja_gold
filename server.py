from flask import Flask, redirect, render_template, request, session, flash
import random
app = Flask(__name__)
app.secret_key = "TheBestPassword"

@app.route('/', methods=['GET', 'POST'])
def main_game():
    if not session.values():
        session['gold'] = int(0)
        session['random'] = int(0)
        print session

    if session['gold'] < int(0):
        positive_version = session['gold'] * -1
        flash('you owe us {} gold. I have confiscated your belongings. Your home...er, I mean my home, is very nice!!'.format(positive_version))
    elif session['random'] >= 0:
        flash('you have earned {} gold! Great!'.format(session['random']))
    elif session['random'] < 0:
        positive_version = session['random'] * -1
        flash('you have lost {} gold, Sucker!'.format(positive_version))

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def roll_the_dice():
    if request.form['btn'] == 'farm':
        random_gold = random.randint(10,21)
        session['random'] = random_gold
        session['gold'] += random_gold
    elif request.form['btn'] == 'cave':
        random_gold = random.randint(5,11)
        session['random'] = random_gold
        session['gold'] += random_gold
    elif request.form['btn'] == 'house':
        random_gold = random.randint(2,6)
        session['random'] = random_gold
        session['gold'] += random_gold
    elif request.form['btn'] == 'casino':
        random_gold = random.randint(-50,51)
        session['random'] = random_gold
        session['gold'] += random_gold
    
    

    return redirect('/')


if (__name__) == ("__main__"):
    app.run(debug=True)