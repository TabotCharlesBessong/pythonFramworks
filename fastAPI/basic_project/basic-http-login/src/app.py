from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    # Here you would typically check the username and password against a database
    if username == 'admin' and password == 'password':  # Example credentials
        return redirect(url_for('success'))
    else:
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('login'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == "__main__":
    app.run(debug=True)