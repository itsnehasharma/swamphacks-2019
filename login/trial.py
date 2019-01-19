from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):

    username = StringField('username')
    password = StringField('password')
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data

        print('hey')

        return redirect(url_for('homepage')) #only for the if statement

    return render_template('trial.html', form=form) #the whole thing


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/homepage')
def homepage():
    if request.method == 'POST':
        if request.form['submit_button'] == '1':
            return redirect(url_for('one'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('two'))

    elif request.method == 'GET':
        return render_template('fake.html', form=form)

    return render_template('homepage.html')

@app.route('/one')
def one():
    return render_template('one.html')

@app.route('/two')
def two():
    return render_template('two.html')


if __name__ == '__main__':
    app.run(debug=True)
