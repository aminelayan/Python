from flask import Flask , render_template, redirect, session

app=Flask(__name__)
app.secret_key='amin'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count= session['count'])

@app.route('/addone')
def addone():
    session['count']
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['count']+=1
    return redirect('/')
@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')


app.run(debug=True)