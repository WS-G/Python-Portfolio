from flask import Flask, render_template, url_for

app = Flask(__name__) #create a Flask instance

@app.route("/")
@app.route("/index.html")
def homepage():
    return render_template('index.html')

@app.route("/contact.html")  #tell Flask what URL should trigger our function
def contact():
    return render_template('contact.html')

@app.route("/components.html")  #tell Flask what URL should trigger our function
def components():
    return render_template('components.html') 

@app.route("/about.html")  #tell Flask what URL should trigger our function
def about():
    return render_template('about.html')

@app.route("/work.html")  #tell Flask what URL should trigger our function
def work():
    return render_template('work.html')

@app.route("/works.html")  #tell Flask what URL should trigger our function
def works():
    return render_template('works.html')