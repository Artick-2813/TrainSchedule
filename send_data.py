from flask import Flask, render_template, request, redirect, url_for
from Parser.ParserTrain import parser, get_title_page
import os

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, InputRequired

SECRET_KEY = os.urandom(30)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


class InputForm(FlaskForm):
    departure = StringField('departure', validators=[Length(min=4, max=50), InputRequired()])
    arrival = StringField('arrival', validators=[Length(min=4, max=50), InputRequired()])
    submit = SubmitField('Показать расписание')


@app.route("/")
def index():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('send_data'))

    return render_template('index.html', form=form)


@app.route("/send_data", methods=['POST'])
def send_data():

    departure = request.form['departure']
    arrival = request.form['arrival']

    info = parser(departure, arrival)
    title = get_title_page()

    if info and title:
        return render_template('show.html', info=info, title=title)

    return render_template('error.html', info=info)
