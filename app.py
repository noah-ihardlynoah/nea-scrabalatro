# "templates" contains html, "static" contains css!!

# imports the flask package
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo

# creates an app instance 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///accounts.db'
app.config['SECRET_KEY'] = "replacemedaddy"
db = SQLAlchemy(app)


# ===========ACCOUNTS DATABASE============
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    # longer than on frontend, bc this is the HASH!!!
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    email = EmailField('Enter your email', validators=[InputRequired(), Length(min=4, max=30)], render_kw={"placeholder":"THIS IS NEWe.g. denreynolds@gmail.com"})
    username = StringField('Enter a unique username', validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"THIS IS NEWe.g. dayman67"})
    password = PasswordField('Enter a strong password', validators=[InputRequired(),EqualTo('confirmPassword', message='Passwords must match'), Length(min=4, max=20)], render_kw={"placeholder":"THIS IS NEWe.g. Password1"})
    confirmPassword = PasswordField('Enter a strong password', validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"THIS IS NEW"})
    submit = SubmitField("THIS IS NEWSign Up")

    def validateUsername(self, username):
        # returns the first name that comes up in username search, or if nothing comes up, returns None
        # adapted from tutorial https://www.youtube.com/watch?v=71EU8gnZqZQ&t=4s
        usernameExists = User.query.filter_by(
            username=username.data).first() 
        if usernameExists:
            raise ValidationError(
                "Username not unique. Choose again."
        )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"THIS IS NEWe.g. dayman67"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"THIS IS NEWe.g. Password1"})
    submit = SubmitField("THIS IS NEWLogin")

    

# ===========END============

# ===========ROUTING============
# default when website domain is loaded, e.g. "youtube.com"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

if __name__ == "__main__":
    # debug=True so that errors are flagged immediately
    app.run(debug=True)
# ===========END============