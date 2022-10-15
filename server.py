from email import message
from lib2to3.pgen2.token import NEWLINE
from urllib import request
from flask import Flask, render_template, send_from_directory, url_for, request, redirect
import os
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def ahtml_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'






"""@app.route('/contact.html')
def contact():
    return render_template('contact.html')"""

"""@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')"""


app.run('127.0.0.1', port = 5050)