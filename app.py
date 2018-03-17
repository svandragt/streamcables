from flask import Flask, session, redirect, url_for, escape, request

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
    return 'login at %s ' % (url_for('login'))


@app.route('/admin')
def admin():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'login at %s ' % (url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('admin'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if me.check(username,password):
            session['username'] = username
            return redirect(url_for('admin'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    me = User('sander', 'loadofcrap')
    app.run()
