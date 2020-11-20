from flask import *
import sys

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('제출용upgrade.html')

@app.route('/my-link/')
def my_link():
     import model_test

     return my_link

if __name__ == '__main__':
    app.run(debug=True)