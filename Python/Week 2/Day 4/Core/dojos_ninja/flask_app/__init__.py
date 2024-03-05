from flask import Flask
app = Flask(__name__)

DATABASE = "dojos_and_ninjas_shema"

app.secret_key = "never ever ever ever give this key"