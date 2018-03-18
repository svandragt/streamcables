

from flask import Flask, session, redirect, url_for, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ, scandir, path

app = Flask(__name__)
app.secret_key = environ['STREAMCABLES_SECRET_KEY']
app.brand = 'StreamCables'


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def check(self, username, password):
        if username != self.username:
            return False
        return check_password_hash(self.pw_hash, password)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manage')
def manage():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']

    cables = read_cables_for_user(username)
    a = 1

    return render_template('manage.html', username=username, cables=cables)


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    if 'username' in session:
        return redirect(url_for('manage'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if me.check(username, password):
            session['username'] = username
            return redirect(url_for('manage'))
    return render_template('login.html', username=username)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



def read_cables_for_user(username):
    folder = '/Users/%s' % username
    onlyfiles = [f.path for f in scandir(folder) if path.splitext(f)[1] == ".json"]

    return onlyfiles

if __name__ == '__main__':
    me = User(environ['STREAMCABLES_ADMIN_USER'], environ['STREAMCABLES_ADMIN_PWD'])
    app.run()
