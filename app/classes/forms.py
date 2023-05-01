# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role',choices=[("Alumni","Alumni"),("Student","Student"),("Site Moderator","Site Moderator")])

class AlumniForm(FlaskForm):
    alfname = StringField('First Name', validators=[DataRequired()])
    allname = StringField('Last Name', validators=[DataRequired()])
    algradyear = IntegerField('Grad Year', validators=[DataRequired()])
    alcollege = StringField('College you attend(ed)')
    almajor = StringField('Your college major')
    alpathway = SelectField('OT Pathway',choices=[("Computer Science","Computer Science"),("Engineering","Engineering"),("FADA","FADA"),("RPL","RPL"),("Health","Health")])
    alsex = SelectField('Sex',choices=[("Male","Male"),("Female","Female"),("Other","Other"),("Prefer not to say","Prefer not to say")])
    alphonenum = IntegerField('Phone Number')
    alemail = StringField('Email')
    allocation = StringField('City of Residence')
    aloccupation = StringField('Current Occupation')
    submit = SubmitField('Submit')



class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    number_of_participants = StringField('Number of Participants', validators=[DataRequired()])
    how_to_join = StringField('How to join', validators=[DataRequired()])
    submit = SubmitField('Submit')

class QAForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Question')


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class AnswerForm(FlaskForm):
    content = TextAreaField('Answer', validators=[DataRequired()])
    submit = SubmitField('Answer')

