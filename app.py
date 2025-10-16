from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def hello_world():
   # return "<p>Hello, World!</p>"
   return render_template('index.html')

@app.route("/login")
def loginpage():
   # return "<p>Hello, World!</p>"
   return render_template('Login.html')

@app.route("/signup")
def signup_form():
    return render_template('SignUp.html')

@app.route("/contact")
def contact_form():
    return render_template('contact-us.html')

@app.route("/dashboard")
def dashboard():
    return render_template('Dashboard.html')


    
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run(debug=True)
