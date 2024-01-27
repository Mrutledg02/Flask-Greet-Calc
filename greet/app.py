from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welconme():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def weclome_back():
    return 'welcome back'

if __name__ == '__main__':
    app.run(debug=True)