from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def show_index():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/')
@app.route('/user/<username>')
def show_user_profile(username=None):
    return render_template('user_profile.html', username=username)


def do_the_login():
    pass

def show_the_login_form():
    pass

if __name__ == '__main__':
    app.run()
