from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__) #create a Flask instance

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def get_page(page_name):
    return render_template(page_name)

def write_to_db(data):
    with open('database.csv', mode='a', newline='') as database: # open file in append mode
        email = data["email"] # creating vars from the "request.form.to_dict" from submit_contact_form func
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) # create the writer object
        csv_writer.writerow([email,subject,message]) # write the 3 vars to the row

@app.route('/contact_submit', methods=['POST', 'GET']) # methods used for the form
def submit_contact_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # get all the data as a dictionary
            write_to_db(data)
            return redirect('submitted.html') #This is the message that will be returned after sending the form
        except:
            return 'database failure, not saved'
    else:
        return '<h2> ERROR - Form Not Submitted! Try Again</h2>' #This is the message returned if there was an ERROR in form submission

