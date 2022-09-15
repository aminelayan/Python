from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def saysth(name):
    return "Hi " + name


@app.route('/repeat/<int:repeat>/<textme>')
def repeatme(repeat, textme):
        return textme * int(repeat)


if __name__ == "__main__":
    app.run(debug=True)
