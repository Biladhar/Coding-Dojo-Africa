from flask import Flask , render_template, redirect, request, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "hello dojo"


# * view route

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def view_counter():
    if "visit" not in session:
        session["visit"]= 0
    else:
        session["visit"] += 1
    return render_template("index.html")  # Return the string 'Hello World!' as a response

# ! action route


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/add",methods=["post"])
def add_1():
    return redirect ("/")

@app.route("/add2",methods=["post"])
def add_2():
    session["visit"] += 1
    return redirect ("/")




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.