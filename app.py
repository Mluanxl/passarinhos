from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def inicio():
    return render_template('index.html')

@app.route("/flor",  methods=["GET", "POST"] )
def flor():
    return render_template("beijaflor.html")

if __name__ == '__main__':
    app.run(debug=True)
