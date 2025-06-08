from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import db, User, StudentProfile
from forms import RegistrationForm, LoginForm, StudentProfileForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
  db.create_all()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_pw = generate_password_hash(form.password.data)
    user = User(username=form.username.data, password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful! Please log in.', 'success')
    return redirect(url_for('login'))
  return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and check_password_hash(user.password, form.password.data):
      login_user(user)
      flash('Logged in successfully.', 'success')
      return redirect(url_for('dashboard'))
    else:
      flash('Invalid username or password.', 'danger')
  return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
  profile = StudentProfile.query.filter_by(user_id=current_user.id).first()
  return render_template('dashboard.html', profile=profile)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def student_profile():
  form = StudentProfileForm()
  profile = StudentProfile.query.filter_by(user_id=current_user.id).first()
  if form.validate_on_submit():
    if not profile:
      profile = StudentProfile(user_id=current_user.id)
    profile.full_name = form.full_name.data
    profile.age = form.age.data
    db.session.add(profile)
    db.session.commit()
    flash('Profile updated!', 'success')
    return redirect(url_for('dashboard'))
  if profile:
    form.full_name.data = profile.full_name
    form.age.data = profile.age
  return render_template('student_profile.html', form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Logged out.', 'info')
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)