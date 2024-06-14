from flask import Flask, render_template, redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Custom admin view
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

# Flask-Admin setup
admin = Admin(app, name='Admin Dashboard', index_view=MyAdminIndexView(), template_mode='bootstrap4')
admin.add_view(ModelView(User, db.session))

# Routes
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/ooh')
def ooh():
    return render_template('ooh.html')

@app.route('/tv')
def tv():
    return render_template('tv.html')

@app.route('/radio')
def radio():
    return render_template('radio.html')

@app.route('/btl')
def btl():
    return render_template('btl.html')

@app.route('/creatives')
def creatives():
    return render_template('creatives.html')

# Create the database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
