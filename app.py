# "templates" contains html, "static" contains css!!

# imports the flask package
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from flask_bcrypt import Bcrypt
import re

# creates an app instance 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///accounts.db'
# URGENT REPLACE NOW
app.config['SECRET_KEY'] = "replacemedaddy"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# user_loader callback used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ===========ACCOUNTS DATABASE============
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    # longer than on frontend, bc this is the HASH!!!
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    # email = EmailField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"class":'textarea', "placeholder":"THIS IS NEWe.g. denreynolds@gmail.com"})
    # username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"THIS IS NEWe.g. dayman67"})
    # password = PasswordField(validators=[InputRequired(),EqualTo('confirmPassword', message='Passwords must match'), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"THIS IS NEWe.g. Password1"})
    # confirmPassword = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"THIS IS NEWe.g.Password1"})
    # submit = SubmitField("THIS IS NEWSign Up", render_kw={"class":'up_register'})

    email = EmailField(validators=[InputRequired(), Length(min=4, max=30)], render_kw={"class":'textarea', "placeholder":"e.g. denreynolds@gmail.com"})
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"e.g. dayman67"})
    password = PasswordField(validators=[InputRequired(),EqualTo('confirmPassword', message='Passwords must match'), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"e.g. Password1"})
    confirmPassword = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"e.g. Password1"})
    submit = SubmitField("THIS IS NEWSign Up", render_kw={"class":'up_register'})

    def validateEmail(self, email):
        # returns the first email that comes up in  search, or if nothing comes up, returns None
        # adapted from tutorial https://www.youtube.com/watch?v=71EU8gnZqZQ&t=4s
        emailExists = User.query.filter_by(
            email=email.data).first() 
        if emailExists:
            raise ValidationError(
                "Email already tied to an account. Try logging in or use a different email."
        )

    def validateUsername(self, username):
        usernameExists = User.query.filter_by(
            username=username.data).first() 
        if usernameExists:
            raise ValidationError(
                "Username not unique. Choose again."
        )

class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Length(min=4, max=50)], render_kw={"class":'textarea', "placeholder":"e.g. denreynolds@gmail.com"})
    # username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"THIS IS NEWe.g. dayman67"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"class":'textarea', "placeholder":"e.g. Password1"})
    submit = SubmitField("Login", render_kw={"class":'up_login'})
 
    

# ===========END============

# ===========ROUTING============
# default when website domain is loaded, e.g. "youtube.com"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    return render_template('account.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # email_or_username = form.username.data
        # email_or_username = email_or_username.lower()
        # # regex to validate emails
        # if re.match("[a-z][a-z0-9]*@[a-z0-9]+.[a-z]+", email_or_username):
        #     user = User.query.filter_by(email=email_or_username).first()
        # else:
        #     user = User.query.filter_by(username=email_or_username).first()

        # WEEWOO AI ALERT STARTS
        user = User.query.filter(
            db.func.lower(User.email) == form.email.data.strip().lower()
        ).first()
        # WEEWOO AI FINISHED HUMAN NOW

        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('account'))

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET','POST'])
@login_required 
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    # hashing is done using Bcrypt - again adapted from https://www.youtube.com/watch?v=71EU8gnZqZQ&t=4s
    if form.validate_on_submit():
        new_user = User(email=form.email.data, username=form.username.data, password=bcrypt.generate_password_hash(form.password.data))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

if __name__ == "__main__":
    # debug=True so that errors are flagged immediately
    app.run(debug=True)
# ===========END============