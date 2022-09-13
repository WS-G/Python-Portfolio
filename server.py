from flask import Flask, render_template, url_for

app = Flask(__name__) #create a Flask instance

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def get_page(page_name):
    return render_template(page_name)