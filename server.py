from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = "gokhansurvey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accept', methods=['POST'])
def accept():
    print(request.form)
    session['name'] = request.form['fullname']
    session['city'] = request.form['city']
    # session['language'] = request.form['language']
    # session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)