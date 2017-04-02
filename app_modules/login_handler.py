from flask import render_template, session, redirect, request


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
            if user_id == 'sid' and password == 'sid123':
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Username & password do not match. Try again'
        elif user_type == 'employer':
            user_id = request.form['e_user_id']
            password = request.form['e_user_pass']
            if user_id == 'google' and password == 'sid123':
                session['username'] = user_id
                session['user_type'] = user_type
                return redirect('/dashboard')
            else:
                error = 'Employer Id & password do not match. Try again'
    return render_template('login.html', error=error)
