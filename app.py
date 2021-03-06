from flask import Flask
from app_modules.homepage import *
from app_modules.login_handler import *
from app_modules.signup_handler import *
from app_modules.dashboard import *
from app_modules.logout_handler import *

app = Flask(__name__)
app.secret_key = '12ka442ka1'  # for session handling

# home page
app.add_url_rule('/', view_func=home, methods=['GET'])
app.add_url_rule('/home', view_func=home, methods=['GET'])

# login & signup & logout
app.add_url_rule('/login/', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/signup/', view_func=signup, methods=['GET', 'POST'])
app.add_url_rule('/logout/', view_func=logout, methods=['GET'])

# dashboard
app.add_url_rule('/dashboard/', view_func=dashboard, methods=['GET'])

if __name__ == '__main__':
    app.run(host='localhost', port=8083, debug=True, threaded=True)
