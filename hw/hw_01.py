from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

 # /user/<name>, который будет возвращать
# приветственное сообщение с переданным именем
@app.route('/user/<name>')
def hello_user(name):
    return f'Hello, {name}'

if __name__ == '__main__':
   app.run()