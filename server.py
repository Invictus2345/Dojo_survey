from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['Your_name']= request.form['Your_name']
    session['Location']= request.form['Location']
    session['Languages']= request.form['Languages']
    session['Comment']= request.form['Comment']
    return redirect('/')

@app.route('/result')
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)