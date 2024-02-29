from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "votre_clé_secrète"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'visits' not in session:
        session['visits'] = 0

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'count':
            session['visits'] += 1
        elif action == 'reset':
            session['visits'] = 0

    return render_template('index.html', visits=session['visits'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


