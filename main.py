from flask import Flask, request, redirect, url_for, session
from flask import render_template

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    if 'username' in session:
         return redirect(url_for('main'))
    else:
        return redirect(url_for('form'))

@app.route("/main/")
def main():
    context = {"username": session["username"]}
    return render_template('main.html', **context)

@app.route("/form/")
def form():
    return render_template('form.html')

@app.route('/save_data/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        if session['username'] != "" and " " not in session['username'] :
            print(session['username'] )
            return redirect(url_for('index'))
    return render_template('form.html')

@app.post('/exit/')
def exit():
    session.pop('username', None)
    return redirect(url_for('form'))