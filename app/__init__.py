from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
# Import statement here is avoid circular import. We import app in views later.
from app import views
