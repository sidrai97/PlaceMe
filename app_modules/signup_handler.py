from flask import render_template, redirect, request, session


def signup():
    error = None
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/dashboard')
    elif request.method == 'POST':
        user_type = request.form['user_type']
        if user_type == 'applicant':
            pass
        elif user_type == 'employer':
            pass
    return render_template('signup.html', error=error)
