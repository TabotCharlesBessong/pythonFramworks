from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response, send_from_directory, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_DOC_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Dummy user store
users = {}

def allowed_file(filename, allowed_set):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_set

@app.errorhandler(404)
def not_found(e):
  return render_template('error.html', code=404, message="Page Not Found"), 404

@app.errorhandler(500)
def server_error(e):
  return render_template('error.html', code=500, message="Internal Server Error"), 500

@app.route('/')
def home():
  if 'username' in session:
    return redirect(url_for('profile'))
  return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username in users:
      flash('Username already exists!', 'danger')
      return redirect(url_for('register'))
    users[username] = {
      'password': password,
      'profile_pic': None,
      'document': None,
      'verified': False
    }
    flash('Registration successful! Please login.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
      session['username'] = username
      resp = make_response(redirect(url_for('profile')))
      resp.set_cookie('last_login', username)
      flash('Login successful!', 'success')
      return resp
    else:
      flash('Invalid credentials!', 'danger')
      return redirect(url_for('login'))
  return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
  if 'username' not in session:
    flash('Please login first.', 'warning')
    return redirect(url_for('login'))
  username = session['username']
  user = users[username]
  if request.method == 'POST':
    # Handle profile picture upload
    if 'profile_pic' in request.files:
      file = request.files['profile_pic']
      if file and allowed_file(file.filename, ALLOWED_IMAGE_EXTENSIONS):
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = secure_filename(f"{username}_profile.{ext}")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user['profile_pic'] = filename  # Only the filename
        flash('Profile picture uploaded!', 'success')
      elif file.filename != '':
        flash('Invalid profile picture format!', 'danger')
    # Handle document upload
    if 'document' in request.files:
      doc = request.files['document']
      if doc and allowed_file(doc.filename, ALLOWED_DOC_EXTENSIONS):
        ext = doc.filename.rsplit('.', 1)[1].lower()
        docname = secure_filename(f"{username}_document.{ext}")
        doc.save(os.path.join(app.config['UPLOAD_FOLDER'], docname))
        user['document'] = docname  # Only the filename
        user['verified'] = True
        flash('Document uploaded! Account verified.', 'success')
      elif doc.filename != '':
        flash('Invalid document format!', 'danger')
  profile_pic = user['profile_pic'] if user['profile_pic'] else 'default_avatar.png'
  verified = user['verified']
  return render_template('profile.html', username=username, profile_pic=profile_pic, verified=verified, document=user['document'])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/logout')
def logout():
  session.clear()
  flash('Logged out successfully.', 'success')
  return redirect(url_for('login'))

if __name__ == '__main__':
  app.run(debug=True)