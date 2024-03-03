from flask import Flask, render_template, redirect ,session ,request

import random


app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def start():
    if "number" not in session:
        session["number"] = random.randint(1, 100) 
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/play_again')
def new_game():
    session.clear()
    return redirect('/')






if __name__=="__main__":       
    app.run(debug=True)    

