from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Event, Comment
from app.classes.forms import EventForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/events')
@login_required
def events():
    events=Event.objects()
    return render_template('events.html', events=events)

@app.route('/event/<eventID>')
@login_required
def event(eventID):
    thisEvent = Event.objects.get(id=eventID)
    return render_template('event.html',event=thisEvent)

@app.route('/event/delete/<eventID>')
# Only run this route if the user is logged in.
@login_required
def eventDelete(eventID):
    # retrieve the blog to be deleted using the blogID
    deleteEvent = Event.objects.get(id=eventID)
    # check to see if the user that is making this request is the author of the blog.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteEvent.author:
        # delete the blog using the delete() method from Mongoengine
        deleteEvent.delete()
        # send a message to the user that the blog was deleted.
        flash('The Event was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete an event you don't own.")
    # Retrieve all of the remaining blogs so that they can be listed.
    events = Event.objects()  
    # Send the user to the list of remaining blogs.
    return render_template('events.html',events=events)

@app.route('/event/new', methods=['GET', 'POST'])
@login_required
def eventNew():

    form = EventForm()
    if form.validate_on_submit():
        newEvent = Event(

            name = form.name.data,
            location = form.name.data,
            time = form.time.data,
            description = form.description.data,
            number_of_participants = form.number_of_participants.data,
            how_to_join = form.how_to_join.data
        )

        newEvent.save()

        return redirect(url_for('event',eventID=newEvent.id))

    return render_template('eventform.html',form=form)


@app.route('/event/edit/<eventID>', methods=['GET', 'POST'])
@login_required
def eventEdit(eventID):
    editEvent = Event.objects.get(id=eventID)

    if current_user != editEvent.author:
        flash("You can't edit an event you don't own.")
        return redirect(url_for('event',eventID=eventID))

    form = EventForm()

    if form.validate_on_submit():

        editEvent.update(
            subject = form.subject.data,
            content = form.content.data,
            tag = form.tag.data,
            modify_date = dt.datetime.utcnow
        )

        return redirect(url_for('event',eventID=eventID))

    form.subject.data = editEvent.subject
    form.content.data = editEvent.content
    form.tag.data = editEvent.tag

    return render_template('eventform.html',form=form)

@app.route('/comment/new/<eventID>', methods=['GET', 'POST'])
@login_required
def commentEventNew(eventID):
    event = Event.objects.get(id=eventID)
    form = CommentForm()
    if form.validate_on_submit():
        commentEventNew = Comment(
            author = current_user.id,
            event = eventID,
            content = form.content.data
        )
        commentEventNew.save()
        return redirect(url_for('event',eventID=eventID))
    return render_template('commentform.html',form=form,event=event)

@app.route('/comment/edit/<commentID>', methods=['GET', 'POST'])
@login_required
def commentEventEdit(commentID):
    editComment = Comment.objects.get(id=commentID)
    if current_user != editComment.author:
        flash("You can't edit a comment you didn't write.")
        return redirect(url_for('event',eventID=editComment.event.id))
    event = Event.objects.get(id=editComment.event.id)
    form = CommentForm()
    if form.validate_on_submit():
        editComment.update(
            content = form.content.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('event',eventID=editComment.event.id))

    form.content.data = editComment.content

    return render_template('commentform.html',form=form,event=event)   

@app.route('/comment/delete/<commentID>')
@login_required
def commentEventDelete(commentID): 
    deleteComment = Comment.objects.get(id=commentID)
    deleteComment.delete()
    flash('The comments was deleted.')
    return redirect(url_for('event',eventID=deleteComment.event.id)) 
