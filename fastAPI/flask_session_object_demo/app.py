from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Dummy user store
users = {}

@app.route('/')
def home():
  return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username in users:
      flash('Username already exists!', 'danger')
      return redirect(url_for('register'))
    users[username] = password
    flash('Registration successful! Please login.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
      session['username'] = username
      flash('Login successful!', 'success')
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid credentials!', 'danger')
      return redirect(url_for('login'))
  return render_template('login.html')

@app.route('/dashboard')
def dashboard():
  if 'username' not in session:
    flash('Please login first.', 'warning')
    return redirect(url_for('login'))
  return render_template('dashboard.html', username=session['username'])

@app.route('/profile')
def profile():
  if 'username' not in session:
    flash('Please login first.', 'warning')
    return redirect(url_for('login'))
  return render_template('profile.html', username=session['username'])

@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
  if 'username' not in session:
    flash('Please login first.', 'warning')
    return redirect(url_for('login'))
  if request.method == 'POST':
    selected_subjects = request.form.getlist('subjects')
    session['subjects'] = selected_subjects
    flash('Subjects updated!', 'success')
    return redirect(url_for('subjects'))
  selected_subjects = session.get('subjects', [])
  return render_template('subjects.html', username=session['username'], selected_subjects=selected_subjects)

@app.route('/logout')
def logout():
  session.clear()
  return render_template('logout.html')

if __name__ == '__main__':
  app.run(debug=True)