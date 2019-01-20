from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from groupfund import db
from groupfund.models import User, Transaction
from groupfund.users.forms import RegistrationForm, LoginForm, UpdateUserForm

users = Blueprint('users',__name__)

#register
@users.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    print('hellooooo')

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering for groupfund!')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


#login
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Login Success')

            next = request.args.get('next') #where did they want to go

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next) #take them to the homepage

    print(form.errors)

    return render_template('login.html', form=form)

#logout
@users.route('/logout')
def logout():
    logout_user() #import from flask_login
    return redirect(url_for('core.index'))
#account

@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()

    if request.method == "GET":
            form.username.data = current_user.username
            form.email.data = current_user.email

    return render_template('account.html', form=form)

@users.route('/finance_center')
@login_required
def finance_center():

    return render_template('finance_center.html')


@users.route("/<username>")
def transaction_history(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    transaction_history = Transaction.query.filter_by(person=user).order_by(Transaction.date.desc()).paginate(page=page, per_page=5)
    return render_template('transaction_history.html', transaction_history=transaction_history, user=user)
