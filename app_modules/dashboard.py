from flask import render_template, session, redirect


def dashboard():
    if 'user_type' in session:
        if session['user_type'] == 'applicant':
            return render_template('applicant_dashboard.html')
        elif session['user_type'] == 'employer':
            return render_template('employer_dashboard.html')
    else:
        return redirect('/login')
