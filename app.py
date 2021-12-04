from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<page>")
def project(page):
    return render_template(page)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        e= data["email"]
        s= data["subject"]
        m= data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([e,s,m])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'something wrong'

