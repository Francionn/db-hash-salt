from app import app, repository
from flask import render_template, url_for, redirect, flash, session
from app.controllers.forms import LoginForm
from app.controllers.form_register import RegisterUser


app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = repository.login(form.email.data, form.password.data)
        if user:
            name = repository.get_name(form.email.data)
            session['username'] = name
            return redirect(url_for('welcome', username=name))

    return render_template('login.html', form=form)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = RegisterUser()
    if form.validate_on_submit():
        user = repository.create_user( form.name.data , form.password.data, form.email.data)
        if user:
            return redirect(url_for('login'))
    return render_template('createacc.html', form=form)

@app.route('/welcome/<username>', methods=['GET'])
def welcome(username):
    if 'username' not in session or session['username'] != username:
        return redirect(url_for('login'))

    return f'Welcome {username} '
