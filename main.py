from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

app.secret_key = b'\xff\x82\x13\xdc\xb0\x8c\x95\t\xfd49\xe8.U\x9a$'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('savepassword'):
            password = request.form['password']
            name = request.form['email']
            return redirect(url_for("test", nm=name, pas=password))
        return redirect(url_for("test"))
    return render_template('SignIn.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('SignUp.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return redirect(url_for("login"))
    return render_template('logout.html')

@app.route('/test')
def test(nm,pas):
    return f"<h1>Password: PROTECTED  name: PROTECTED <\h1>"

@app.route('/test/<nm>/<pas>')
def test(nm,pas):
    return f"<h1>Password: {pas}  name: {nm}<\h1>"

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found"

if __name__ == '__main__':
    app.run(debugMode=True)
