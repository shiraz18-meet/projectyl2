from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
heroku = Heroku(app)
db = SQLAlchemy(app)

# Create our database model
class Summary(db.Model):
    __tablename__ = "summary"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    subject = db.Column(db.String())
    title = db.Column(db.String())
    picture = db.Column(db.String())
    summary = db.Column(db.String())

    def __init__(self, name):
        self.name = name
    def __init__(self, subject):
        self.subject = subject
    def __init__(self, title):
        self.title = title
    def __init__(self, picture):
        self.picture = picture
    def __init__(self, summary):
        self.summary = summary


# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('project.html')

@app.route('/about')
def about():
    return render_template('About_us.html')

@app.route('/submit')
def submit():
    return render_template('Submit_Summary.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()