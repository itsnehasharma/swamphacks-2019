#payments/views.py
from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from groupfund import db
from groupfund.models import Transaction
from groupfund.transactions.forms import TransactionForm

transactions = Blueprint('transactions', __name__)

# make a payment
@transactions.route('/make_payment', methods=['GET', 'POST'])
@login_required
def make_payment():

    form  = TransactionForm()

    if form.validate_on_submit():

        #print(form.amount.data)
        payment = Transaction(amount=form.amount.data,
                                notes=form.notes.data,
                                user_id=current_user.id)

        db.session.add(payment)
        db.session.commit()
        print(payment)

        return redirect(url_for('users.account'))

    return render_template('make_payment.html', form=form)


@transactions.route('/<int:transaction_id>')
def transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)

    return render_template('transaction.html', amount = transaction.amount,
                                        date = transaction.date,
                                        transaction = transaction)


# @transactions.route('/transaction_history')
# def transaction_history():
#
#     form = TransactionForm()
#
#     transactions = Transaction.query.filter_by(user_id = current_user.id)
#     print(transactions)
#
#     return render_template('transaction_history.html', transactions=transactions)
