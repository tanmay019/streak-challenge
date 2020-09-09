from flask import Flask
app = Flask(__name__)

def main():
    app.run()

@app.route('/')
def greet():
    return "Hello world"