from flask import Flask, render_template, request, redirect
from flask_login import current_user 
from models import User, db, login

app = Flask(__name__)

app.secret_key = 'thismustbesecret'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login.init_app(app)
login.login_view = 'login' 

@app.before_first_request
def fill_db():
  db.create_all()

def products():
  return render_template("product.html", products=products)

def login():
  if current_user.is_authenticated:
    return
  
  if request.method == 'POST':
    email = request.form['email']
    user = User.query.filter_by(email = email).first()

    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
  if current_user.is_authenticated:
    return redirect('/product')

  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    if User.query.filter_by(email=email).first():
      return redirect('register')

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect('/login')

  return render_template('register.html')


if __name__ == '__main__':
  app.run(debug=True)
