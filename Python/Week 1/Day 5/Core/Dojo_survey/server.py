from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'never ever ever give this'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['form_data'] = request.form
    return redirect('/result')

@app.route('/result')
def result():
    form_data = session.get('form_data')
    return render_template('result.html', form_data=form_data)



if __name__ == '__main__':
    app.run(debug=True)