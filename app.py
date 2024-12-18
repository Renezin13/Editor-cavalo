from flask import Flask, url_for, render_template, request, redirect
from flask_login import login_required, login_user, LoginManager, logout_user
from models import *
from database import *

app = Flask(__name__)

app.secret_key = "SUPERMEGASECRETO"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter_by(id=user_id).first()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    user = session.query(User).filter_by(email=email).first()

    if user.email and check_password_hash(user.password, password):
      login_user(user)
      return redirect(url_for('dashboard'))

  return render_template('login.html')

@app.route('/register', methods=["GET","POST"])
def register():
  if request.method == "POST":
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    user = User(name=name, email=email, senha=password)
    session.add(user)
    session.commit()

    return redirect(url_for('register'))
  
  return render_template('register.html')

@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        name = request.form['name']
        race = request.form['race']
        cavalo = Cavalo(name=name, race=race)
        session.add(cavalo)
        session.commit()
        return redirect(url_for('dashboard'))
    horses = session.query(Cavalo).all()
    return render_template('dashboard.html', horses=horses)

@app.route('/dashboard/edit/<int:id>', methods=["GET", "POST"])
@login_required
def edit_cavalo(id):
    cavalo = session.query(Cavalo).get(id)
    if request.method == "POST":
        cavalo.name = request.form['name']
        cavalo.race = request.form['race']
        session.commit()
        return redirect(url_for('dashboard'))
    return render_template('edit_cavalo.html', cavalo=cavalo)

@app.route('/dashboard/delete/<int:id>', methods=["POST"])
@login_required
def delete_cavalo(id):
    cavalo = session.query(Cavalo).get(id)
    session.delete(cavalo)
    session.commit()
    return redirect(url_for('dashboard'))
