from flask import render_template, session, redirect, request
# from flask.ext.bcrypt import check_password_hash
from app_modules.db_connection import *


def login():
    error = None
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/dashboard')
    elif request.method == 'POST':
        user_type = request.form['user_type']
        if user_type == 'applicant':
            user_id = request.form['a_user_id']
            password = request.form['a_user_pass']
            # checking if user has an entry in applicants collection
            res = applicants.find_one({"_id": user_id, "password": password}, {"_id": 1, "password": 1})
            # print(res)
            if res is not None:
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Username & password do not match. Try again'
        elif user_type == 'employer':
            user_id = request.form['e_user_id']
            password = request.form['e_user_pass']
            # checking if user has an entry in employers collection
            res = employers.find_one({"_id": user_id, "password": password}, {"_id": 1, "password": 1})
            # print(res)
            if res is not None:
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Employer Id & password do not match. Try again'
    return render_template('login.html', error=error)
