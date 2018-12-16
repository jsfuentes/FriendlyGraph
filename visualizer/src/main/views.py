from flask import Blueprint, render_template, request, flash, redirect, url_for
from .utils import getFriendData

main = Blueprint('main', __name__)

@main.route('/')
def index():
    friends = getFriendData()
    return render_template("index.html", friends = friends)