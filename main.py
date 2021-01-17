from flask import Flask, url_for, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def template_page(page_name):
    if page_name.find('.') !=-1:
        return render_template(page_name)
    else:
        return render_template(page_name + '.html')

def write_to_txt(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as f:
        f.write(f'{email}, {subject}, {message}')
        f.write('\n')


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.csv', 'a', newline = '') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        data = request.form.to_dict()
        write_to_txt(data)
        write_to_csv(data)
        return redirect('thank_you.html')
    else:
        return "went wrong"


# @app.route('/works')
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
# @app.route('/work')
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
# @app.route('/about')
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

