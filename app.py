# "templates" contains html, "static" contains css!!

# imports the flask package
from flask import Flask, render_template


# creates an app instance
app = Flask(__name__)


# ===========ROUTING============
# default when website domain is loaded, e.g. "youtube.com"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == "__main__":
    # debug=True so that errors are flagged immediately
    app.run(debug=True)
# ===========END============