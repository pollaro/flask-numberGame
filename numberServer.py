from flask import Flask, render_template, request, redirect, session
import random,os
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    if session.has_key('answer'):
        hint = session['hint']
    else:
        session['answer'] = random.randint(0,101)
        print session['answer']
        hint = 'none'
    return render_template('index.html',hint=hint)

@app.route('/guess',methods=['POST'])
def guessing():
    if int(request.form['guessIn']) < int(session['answer']):
        session['hint'] = 'low'
    elif int(request.form['guessIn']) > int(session['answer']):
        session['hint'] = 'high'
    else:
        session['hint'] = 'win'
    return redirect('/')

@app.route('/reset',methods=['POST'])
def reset():
    del session['answer']
    del session['hint']
    return redirect('/')

app.run(debug=True)
