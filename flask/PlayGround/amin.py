from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
  return 'Welcome to The PlayGround'

@app.route('/play')
def play_3():
  return render_template('play.html', times=3)

@app.route('/play/<number>')
def play_number(number):
  number = int(number)
  return render_template("play.html", times=number)

@app.route('/play/<number>/<color>')
def play_color(number, color):
  number = int(number)
  return render_template("play.html", times=number, color=color)

if __name__=="__main__":
  app.run(debug=True)