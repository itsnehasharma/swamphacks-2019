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

        return redirect(url_for('thankyou')) #only for the if statement

    return render_template('trial.html', form=form) #the whole thing


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
