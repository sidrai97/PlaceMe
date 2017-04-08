from flask import render_template, session, redirect


def dashboard():
    if 'user_type' in session:
        if session['user_type'] == 'applicant':
            user_id = session['username']
            return render_template('applicant_dashboard.html', user_id = user_id)
        elif session['user_type'] == 'employer':
            user_id = session['username']
            return render_template('employer_dashboard.html', user_id = user_id)
    else:
        return redirect('/login')
