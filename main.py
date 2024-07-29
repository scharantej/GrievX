
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('complaint_form.html')

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    name = request.form['name']
    email = request.form['email']
    complaint = request.form['complaint']

    # Save complaint to database or other persistent storage

    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
