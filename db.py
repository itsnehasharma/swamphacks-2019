#payments/views.py
from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from groupfund import db
from groupfund.models import Transaction, User, Group
from groupfund.transactions.forms import TransactionForm

User.query.delete()
Transaction.query.delete()
Group.query.delete()
