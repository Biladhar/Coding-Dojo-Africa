from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index(row=8,col=8):
    return render_template("index.html",x = row,y=col)

@app.route('/<int:x>')
def number_of_row(x,col=8):
    return render_template("index.html",x=x, y=col)

@app.route('/<int:x>/<int:y>')
def number_of_rc(x,y):
    return render_template("index.html",x=x, y=y)



if __name__=="__main__":
    app.run(debug=True)