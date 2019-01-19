# groupfund/__init__.py
from flask import Flask

app = Flask(__name__)


from groupfund.core.views import core #importing blueprint
app.register_blueprint(core)
