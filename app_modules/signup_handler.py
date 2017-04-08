from flask import render_template, redirect, request, session
from app_modules.db_connection import *


def signup():
    error = None
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/dashboard')
    elif request.method == 'POST':
        user_type = request.form['user_type']
        if user_type == 'applicant':
            user_id = request.form['a_id']
            name = request.form['a_name']
            email = request.form['a_email']
            tel = request.form['a_tel']
            password = request.form['a_pass']
            # check db
            res = applicants.find_one({"_id": user_id}, {"_id": 1})
            if res is None:
                # robust write left
                applicants.insert_one({"_id": user_id, "name": name, "email": email, "tel": tel, "password": password})
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Username already taken. Try a different one'
        elif user_type == 'employer':
            user_id = request.form['e_id']
            org = request.form['e_org']
            name = request.form['e_name']
            tel = request.form['e_tel']
            email = request.form['e_email']
            password = request.form['e_pass']
            # check db
            res = employers.find_one({"_id": user_id}, {"_id": 1})
            if res is None:
                # robust write left
                employers.insert_one({"_id": user_id, "org": org, "name": name, "email": email, "tel": tel,
                                      "password": password})
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Login ID already taken. Try a different one'
    return render_template('signup.html', error=error)
