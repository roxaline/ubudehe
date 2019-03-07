from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Citizen,Searched
from . import main
from .forms import PitchForm,CommentForm,VoteForm,UpdateProfile,CPitchForm,RPitchForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The pitches Website Online'
    # pitches = Pitch.query.all()
    # form1 = PitchForm()
    # category=form1.category.data
    # pitchesC1=Pitch.query.filter_by(category='P').all()
    # pitchesC2=Pitch.query.filter_by(category='C').all()
    # pitchesC3=Pitch.query.filter_by(category='R').all()

    # users= None
    # for pitch in pitchesC1:
    #     comments=Comment.query.filter_by(pitch_id=pitch.id).all()
    #     return render_template('index.html', title = title,pitchesC1=pitchesC1, users=users,comments=comments)
    #
    # for pitch in pitchesC2:
    #     comments=Comment.query.filter_by(pitch_id=pitch.id).all()
    #     return render_template('index.html', title = title,pitchesC2=pitchesC2, users=users,comments=comments)
    #
    # for pitch in pitchesC3:
    #     comments=Comment.query.filter_by(pitch_id=pitch.id).all()
    #     return render_template('index.html', title = title,pitchesC3=pitchesC3, users=users,comments=comments)

    return render_template('index.html', title = title)
# from flask import Flask
# app = Flask(__name__)
# app.debug = True

# @main.route('/')
# def hello_world():
#     return 'Hello, World!'
#
# def main():
#     app.run()
#
# if __name__ == '__main__':
#     main()
#
@main.route('/user/<uname>/')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # user = User.query.all()
    # pitchesC1=Pitch.query.filter_by(category='P').all()
    # pitchesC2=Pitch.query.filter_by(category='C').all()
    # pitchesC3=Pitch.query.filter_by(category='R').all()
    # print(pitchesC1)
    # pitches=Pitch.query.filter_by(user_id=id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/bio',methods = ['GET','POST'])
@login_required
def update_bio(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_bio.html',form =form)

# @main.route('/new_pitch/',methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form1 = PitchForm()
#     form2 = CPitchForm()
#     form3 = RPitchForm()
#
#     P=pitchesC1=Pitch.category='P'
#     C=pitchesC2=Pitch.category='C'
#     R=pitchesC3=Pitch.category='R'
#     if form1.validate_on_submit():
#         pitch = Pitch(name = form1.name.data, user_id = current_user.id,category=form1.category.data)
#         db.session.add(pitch)
#         db.session.commit()
#         return redirect(url_for('.index'))
#     elif form2.validate_on_submit():
#         pitch = Pitch(name = form2.name.data, user_id = current_user.id,category='C')
#         db.session.add(pitch)
#         db.session.commit()
#         return redirect(url_for('.index'))
#     elif form3.validate_on_submit():
#         pitch = Pitch(name = form3.name.data, user_id = current_user.id,category='R')
#         db.session.add(pitch)
#         db.session.commit()
        # upvote = Vote(upvote = form.validate_on_submit(),pitch_id = pitch.id)
        # downvote = Vote(downvote = form.validate_on_submit(),pitch_id = pitch.id)
        # up=0
        # down=0
        # for upvote in vote:
        #     up+=1
        #     upvote=up
        #     db.session.add(upvote=up)
        #     db.session.commit()
        # for downvote in vote:
        #     down+=1
        #     downvote=down
        #     db.session.add(downvote=down)
        #     db.session.commit()
        # user=User.query.filter_by(id = pitch.id).first()
        # return redirect(url_for('.new_pitch',uname=user.username))
    #     return redirect(url_for('.index'))
    # else:
    #     print("ok")
    # return render_template('profile/new_pitch.html',pitch_form=form1,Cpitch_form=form2,Rpitch_form=form3,pitchesC1=pitchesC1,pitchesC2=pitchesC2,pitchesC3=pitchesC3,P=P,C=C,R=R)

# @main.route('/new_comment/<int:id>',methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     form = CommentForm()
    # pitchesC1=get_pitch('P')
    # pitchesC2=get_pitch('C')
    # pitchesC3=get_pitch('R')

    # pitchesC1=Pitch.query.filter_by(category='P',id=id).all()
    # pitchesC2=Pitch.query.filter_by(category='C',id=id).all()
    # pitchesC3=Pitch.query.filter_by(category='R',id=id).all()
    # pitches=Pitch.query.filter_by(id=id).all()
    # comments=Comment.query.filter_by(pitch_id=id).all()
    # if form.validate_on_submit():
    #     comment = Comment(name = form.name.data, pitch_id = id)
    #     db.session.add(comment)
    #     db.session.commit()
    #     return redirect(url_for('.index'))
    #
    # return render_template('profile/new_comment.html',comment_form=form,comments=comments,pitchesC1=pitchesC1,pitchesC2=pitchesC2,pitchesC3=pitchesC3,pitches=pitches)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))




def search_citizen(ID):
    citizen = Citizen.query.filter_by(ID = ID).first()
    search_citizen_results = None

    if search_citizen_response['citizens']:
        search_citizen_list = search_citizen_response['citizens']
        search_citizen_results = citizen(fname,lname,ID,insurance)


    return search_citizen_results
