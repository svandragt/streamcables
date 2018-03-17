from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

app.secret_key = 'zlToE1fsKn3984jDdt'

from werkzeug.security import generate_password_hash, \
     check_password_hash


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def check(self, username,password):
        if (username != self.username):
            return False
        return check_password_hash(self.pw_hash, password)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    return render_template('admin.html', username=username)



@app.route('/login', methods=['GET', 'POST'])
def login():
    username = ''
    if 'username' in session:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if me.check(username,password):
            session['username'] = username
            return redirect(url_for('admin'))
    return render_template('login.html', username=username)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    me = User('sander', 'loadofcrap')
    app.run()
