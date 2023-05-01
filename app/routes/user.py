from app import app
from flask_login.utils import login_required
from flask import render_template, redirect, flash, url_for
from app.classes.data import User
from app.classes.forms import ProfileForm
from flask_login import current_user

# These routes and functions are for accessing and editing user profiles.

# The first line is what listens for the user to type 'myprofile'
@app.route('/myprofile')
# This line tells the user that they cannot access this without being loggedin
@login_required
# This is the function that is run when the route is triggered
def myProfile():
    # This sends the user to their profile page which renders the 'profilemy.html' template
    return render_template('profilemy.html')
@app.route('/alumni/edit', methods=['GET','POST'])
@login_required
def alumniEdit():
    form = AlumniForm()
    currUser = current_user
    if form.validate_on_submit():
        currUser.update(
            alfname = form.alfname.data,
            allname = form.allname.data,
            algradyear = form.algradyear.data,
            alcollege = form.alcollege.data,
            almajor = form.almajor.data,
            alpathway = form.alpathway.data,
            alsex = form.alsex.data,
            alphonenum = form.alphonenum.data,
            alemail = form.alemail.data,
            allocation = form.allocation.data,
            aloccupation = form.aloccupation.data
        )

        # Then sends the user to their profle page
        return redirect(url_for('myProfile'))
    
    form.alfname.data = current_user.alfname
    form.allname.data = current_user.allname
    form.algradyear.data = current_user.algradyear
    form.alcollege.data = current_user.alcollege
    form.almajor.data = current_user.almajor
    form.alpathway.data = current_user.alpathway
    form.alsex.data = current_user.alsex
    form.alphonenum.data = current_user.alphonenum
    form.alemail.data = current_user.alemail
    form.allocation.data = current_user.allocation
    form.aloccupation.data = current_user.aloccupation
    return render_template('alumniform.html', form=form)
# This is the route for editing a profile
# the methods part is required if you are using a form 
@app.route('/myprofile/edit', methods=['GET','POST'])
# This requires the user to be loggedin
@login_required
# This is the function that goes with the route
def profileEdit():
    # This gets an object that is an instance of the form class from the forms.pyin classes
    form = ProfileForm()
    # This asks if the form was valid when it was submitted
    if form.validate_on_submit():
        # if the form was valid then this gets an object that represents the currUser's data
        currUser = User.objects.get(id=current_user.id)
        # This updates the data on the user record that was collected from the form
        currUser.update(
            lname = form.lname.data,
            fname = form.fname.data,
        )
        # This updates the profile image
        if form.image.data:
            if currUser.image:
                currUser.image.delete()
            currUser.image.put(form.image.data, content_type = 'image/jpeg')
            # This saves all the updates
            currUser.save()
        # Then sends the user to their profle page
        return redirect(url_for('myProfile'))

    # If the form was not submitted this prepopulates a few fields
    # then sends the user to the page with the edit profile form
    form.fname.data = current_user.fname
    form.lname.data = current_user.lname
    form.role.data = current_user.role

    currUser.update(
            lname = form.lname.data,
            fname = form.fname.data,
            role = form.role.data
        )

    return render_template('profileform.html', form=form)

# @app.route('/alumniprofiles')
# def alumniProfiles():
#     users = User.objects()
#     return render_template('alumniprofiles.html',users=users)