from flask import Flask, session, redirect, url_for, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ

app = Flask(__name__)
app.secret_key = environ['secret_key']
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
    return render_template('manage.html', username=username)


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


if __name__ == '__main__':
    me = User(environ['admin_user'], environ['admin_pwd'])
    app.run()