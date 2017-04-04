from flask import session, redirect


def logout():
    session.pop('username', None)
    session.pop('user_type', None)
    return redirect('/login')