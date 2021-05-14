'''
Kelso du Mez
3/05/2021 - (date when finished)
SQLAlchemy Go Website (hopefully)
'''
from flask import Flask, render_template, session, redirect, url_for, request, Blueprint, flash
from random import randint, choice
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, Column, Integer
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # defines db as sqlalchemy connection to database

import models

@app.route('/')
def home():
    return render_template('home.html')

'''
    def current_user(): # function to create a session for user
        if session.get("user"):
            # gotta do the login stuff first for any of this to make sense

    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        if session.get('user'):
            return redirect('/')

    @app.route('/logout')
    def logout():
'''

@app.route('/createaccount', methods = ['GET', 'POST']) 
def createaccount():
    if request.method == 'POST':
        if 5 > len(request.form.get('username')) > 12: # if the length of the inputted username is lesser than 5 and greater than 12 (characters)
            return render_template('createaccount.html', error = 'username must be between 5 and 12 characters') # account will not be created with said username and user is prompted to input a shorter/longer username     
        elif models.users.query.filter(models.users.username == request.form.get('username')).first(): # if the username already exists in the db
            return render_template('createaccount.html', error = 'username already in use') # account will not be created and user is prompted to use a different username
        elif len(request.form.get('password')) < 7: #
            return render_template('createaccount.html', error = 'password must be a minimum of 7 characters') 
        else:
            user_info = models.users (
                username = request.form.get('username'), # takes username from form
                password = generate_password_hash(request.form.get('password'), salt_length = 10), # takes password inputted in form and salts and hashes it for encryption
                gamesWon = 0, gamesLost = 0 
                )
            db.session.add(user_info)
            db.session.commit()
    return render_template('createaccount.html')
    
'''
    @app.route('/game/<int:gameId>')

    @app.route('/selectgame')

    @app.route('/leaderboard')

    @app.route('/createaccount')
'''

if __name__ == "__main__": 
    app.run(debug=True) # runs with debug active so i can tell how bad my code is