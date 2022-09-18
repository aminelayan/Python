from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    dojo_location = request.form['location']
    favorite_lang = request.form['language']
    comment_box = request.form['comment']
    return render_template("submit.html", name_on_template=name_from_form, location_on_template=dojo_location, lang_on_template=favorite_lang, comment_on_template=comment_box)


if __name__ == "__main__":
    app.run(debug=True)