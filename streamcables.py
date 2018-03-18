from os import environ, scandir, path

from flask import Flask, session, redirect, url_for, request, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.update(
    SECRET_KEY =environ['STREAMCABLES_SECRET_KEY']
)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/manage')
def manage():
    if 'username' not in session:
        return redirect(url_for('login'))

    cables = read_cables_for_user(session['username'])

    return render_template('manage.html', cables=cables)


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
    flash('Incorrect login, please try again.','important')
    return render_template('login.html', username=username)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


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


def read_cables_for_user(username):
    """
    Build an list of cables for the specified user
    :param username: string
    :return: list of cables
    """
    folder = '/Users/{u}'.format(u=username)
    cables = [f.path for f in scandir(folder) if path.splitext(f)[1] == ".json"]
    return cables


@app.context_processor
def inject_project_meta():
    return dict(project_name='StreamCables')


if __name__ == '__main__':
    me = User(environ['STREAMCABLES_ADMIN_USER'], environ['STREAMCABLES_ADMIN_PWD'])
    app.run()
