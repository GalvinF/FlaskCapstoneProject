from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import QA, Answer
from app.classes.forms import QAForm, AnswerForm
from flask_login import login_required
import datetime as dt

@app.route('/qa/list')
@app.route('/qas')

@login_required
def qaList():
    qas = QA.objects()
    return render_template('qas.html',qas=qas)

@app.route('/qa/<qaID>')

@login_required
def qa(qaID):
    thisQA = QA.objects.get(id=qaID)
    theseAnswers = Answer.objects(qa=thisQA)
    return render_template('qa.html',qa=thisQA,answers=theseAnswers)

     
@app.route('/qa/delete/<qaID>')
@login_required
def qaDelete(qaID):
    deleteQA = QA.objects.get(id=qaID)
    if current_user == deleteQA.author:
        deleteQA.delete()
        flash('The question was deleted.')
    else:
        flash("You can't delete a blog you don't own.")
    qas = QA.objects()  
    # Send the user to the list of remaining blogs.
    return render_template('qas.html',qas=qas)