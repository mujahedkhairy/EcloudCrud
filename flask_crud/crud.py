import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, flash
from db import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


from models import User


with app.app_context():
    db.create_all()



class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@app.route('/create', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('get_users'))
    return render_template('user_form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            user.active = True  # Set user to active
            print(f"User {user.username} is now active.")
            db.session.commit()  # Commit the changes
            return redirect(url_for('get_users'))  # Redirect to user list or dashboard
    return render_template('login.html', form=form)



@app.route('/logout/<int:id>')
def logout(id):
    user = User.query.get_or_404(id)
    user.active = False
    db.session.commit()
    return redirect(url_for('get_users'))



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    form = UserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        db.session.commit()
        return redirect(url_for('get_users'))
    form.username.data = user.username
    form.password.data = user.password
    return render_template('user_form.html', form=form)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        # If the form is submitted, delete the user
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")
        return redirect(url_for('get_users'))

    # Render the confirmation template
    return render_template('user_confirm_delete.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
