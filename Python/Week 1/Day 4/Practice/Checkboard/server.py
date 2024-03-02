from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def number_of_rcolor(x=8,y=8,color1="black",color2="white"):
    return render_template("index.html",x=x, y=y, color0 = color1 , color1 = color2)



if __name__=="__main__":
    app.run(debug=True)