from flask import Flask

app = Flask(__name__)

from app import routes # must be below app=flask(__name__)
