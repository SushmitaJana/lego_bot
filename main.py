from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def load():
    return render_template('a.html')


if __name__ == '__main__':
   app.run(debug = False, host='0.0.0.0')