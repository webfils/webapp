#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

from form_contact import ContactForm, csrf

mail = Mail()

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = '5kRicVKYezeoy7sHm6eks551IIjp5IInCAxL1-_0nmw'
csrf.init_app(app)

app.config['MAIL_SERVER']='mail.webfils.com'
app.config['MAIL_PORT'] = 26
app.config['MAIL_USERNAME'] = 'gary@webfils.com'
app.config['MAIL_PASSWORD'] = '@Gary2016'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False

mail.init_app(app)

posts = [
    {
        'author': 'Corney Cox',
        'title': 'First Commit',
        'content': ' My First Content Flask',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Gary Aven',
        'title': 'Second Commit',
        'content': ' My Second Content Flask',
        'date_posted': 'April 23, 2021'
    }
]

@app.route('/')
def home():
    title = 'Webfils'
    return render_template('pages/home.html', title=title, posts=posts)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():        
        print('-------------------------')
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['message'])       
        print('-------------------------')
        send_message(request.form)
        return redirect('/success')    

    return render_template('pages/contact.html', form=form)

@app.route('/success')
def success():
    return render_template('pages/home.html')

@app.route('/services')
def services():
    title = 'Our Services'
    return render_template('pages/services.html', title=title)

def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['info@webfils.com'],
            body= message.get('message')
    )  
    mail.send(msg)

if __name__ == "__main__":
    app.run(debug = True)