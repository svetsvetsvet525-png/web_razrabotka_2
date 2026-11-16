from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/one')
def one():
    return 'Hello world'

@app.route('/two')
def two():
    return 'Hi'

@app.route('/user/<username>')
def user_profile(username):
    return render_template('hello.html', name=username)

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form(['name'])
    return f'Hello {name}'

@app.route('/index')
def index():
    user = {'username':'s'}
    post = [{'autor': {'username': 'Тим Кук'}, 'body': 'a'},
                {'autor': {'username': 'Илон Макс'}, 'body': 'b'}]
    return render_template('index.html', title='Home', user=user, posts=post)



if __name__ == '__main__':
    app.run(debug=True)