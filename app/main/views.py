from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitch,Comment
from . import main
from .forms import PitchForm,CommentForm,VoteForm,UpdateProfile,CPitchForm,RPitchForm
from .. import db,photos
from flask_login import login_required,current_user
import markdown2
# from flask import Flask
# app = Flask(__name__)
# app.debug = True
#

@main.route('/',methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The pitches Website Online'
    pitches = Pitch.query.all()
    pitchesC1=Pitch.query.filter_by(category='P').all()
    pitchesC2=Pitch.query.filter_by(category='C').all()
    pitchesC3=Pitch.query.filter_by(category='R').all()
    users= None
    for pitch in pitchesC1:
        comments=Comment.query.filter_by(pitch_id=pitch.id).all()
        return render_template('index.html', title = title,pitchesC1=pitchesC1, users=users,comments=comments,pitches=pitchesC1)

    for pitch in pitchesC2:
        comments=Comment.query.filter_by(pitch_id=pitch.id).all()
        return render_template('index.html', title = title,pitchesC2=pitchesC2, users=users,comments=comments,pitches=pitchesC2)

    for pitch in pitchesC3:
        comments=Comment.query.filter_by(pitch_id=pitch.id).all()
        return render_template('index.html', title = title,pitchesC3=pitchesC3, users=users,comments=comments,pitches=pitchesC1)

    return render_template('index.html', title = title,pitchesC3=pitchesC3, users=users,allinone=allinone)
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
    pitchesC1=Pitch.query.filter_by(category='P').all()
    pitchesC2=Pitch.query.filter_by(category='C').all()
    pitchesC3=Pitch.query.filter_by(category='R').all()
    # pitches=Pitch.query.filter_by(user_id=id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches=pitchesC1)

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

# @main.route('/user/update/pitch/<id>',methods = ['GET','POST'])
# def single_review(id):
#     pitch=Pitch.query.get(id)
#     if pitch is None:
#         abort(404)
#     form = PitchForm()
#
#     if form.validate_on_submit():
#         user.pitches = form.pitches.data
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('.profile',pitch=user.pitches))
#
#     format_pitch = markdown2.markdown(pitch.movie_pitch,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('new_pitch.html',pitch = pitch,format_pitch=format_pitch)

@main.route('/new_pitch/',methods = ['GET','POST'])
@login_required
def new_pitch():
    form1 = PitchForm()
    form2 = CPitchForm()
    form3 = RPitchForm()

    P=pitchesC1=Pitch.query.filter_by(category='P').all()
    C=pitchesC2=Pitch.query.filter_by(category='C').all()
    R=pitchesC3=Pitch.query.filter_by(category='R').all()
    pitches=Pitch.query.filter_by(category='P').all()
    # users=User.query.filter_by(id=id).all()
    if form1.validate_on_submit():
        pitch = Pitch(name = form1.name.data, user_id = current_user.id,category='P')
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('.index'))
    if form2.validate_on_submit():
        pitch = Pitch(name = form2.name.data, user_id = current_user.id,category='C')
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('.index'))
    if form3.validate_on_submit():
        pitch = Pitch(name = form3.name.data, user_id = current_user.id,category='R')
        db.session.add(pitch)
        db.session.commit()
        upvote = Vote(upvote = form.validate_on_submit(),pitch_id = pitch.id)
        downvote = Vote(downvote = form.validate_on_submit(),pitch_id = pitch.id)
        up=0
        down=0
        for upvote in vote:
            up+=1
            upvote=up
            db.session.add(upvote=up)
            db.session.commit()
        for downvote in vote:
            down+=1
            downvote=down
            db.session.add(downvote=down)
            db.session.commit()
        user=User.query.filter_by(id = pitch.id).first()
        return redirect(url_for('.new_pitch',uname=user.username))
        return redirect(url_for('.index'))
    return render_template('profile/new_pitch.html',pitch_form=form1,Cpitch_form=form2,Rpitch_form=form3,pitchesC1=pitchesC1,pitchesC2=pitchesC2,pitchesC3=pitchesC3,pitches=pitches,P=P,C=C,R=R)

# @main.route('/new_pitch/r',methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = RPitchForm()
#
#     if form.validate_on_submit():
#         pitch = Pitch(name = form.name.data, user_id = current_user.id)
#         db.session.add(pitch)
#         db.session.commit()
#         user=User.query.filter_by(id = current_user.id).first()
#         return redirect(url_for('.new_pitch',uname=user.username))
#
#         # return redirect(url_for('.index'))
#     return render_template('profile/new_pitch.html',Rpitch_form=form)

# @main.route('/new_pitch/c',methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = CPitchForm()
#
#     if form.validate_on_submit():
#         pitch = Pitch(name = form.name.data, user_id = current_user.id)
#         db.session.add(pitch)
#         db.session.commit()
#         user=User.query.filter_by(id = current_user.id).first()
#         return redirect(url_for('.new_pitch',uname=user.username))
#
#         # return redirect(url_for('.index'))
#     return render_template('profile/new_pitch.html',Cpitch_form=form)


@main.route('/new_comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    # pitchesC1=get_pitch('P')
    # pitchesC2=get_pitch('C')
    # pitchesC3=get_pitch('R')

    pitchesC1=Pitch.query.filter_by(category='P',id=id).all()
    pitchesC2=Pitch.query.filter_by(category='C',id=id).all()
    pitchesC3=Pitch.query.filter_by(category='R',id=id).all()
    pitches=Pitch.query.filter_by(id=id).all()
    comments=Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():
        comment = Comment(name = form.name.data, pitch_id = id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('profile/new_comment.html',comment_form=form,comments=comments,pitchesC1=pitchesC1,pitchesC2=pitchesC2,pitchesC3=pitchesC3,pitches=pitches)

# @main.route('/new_vote/',methods = ['GET','POST'])
# @login_required
# def new_vote():
#     form = VoteForm()
#     # votes = get_vote(id)
#
#     if form.validate_on_submit():
#         pitch = Pitch(name = form.name.data, user_id = current_user.id)
#         upvote = Vote(upvote = form.validate_on_submit(),pitch_id = pitch.id)
#         downvote = Vote(downvote = form.validate_on_submit(),pitch_id = pitch.id)
#         up=0
#         down=0
#         for upvote in vote:
#             up+=1
#             db.session.add(upvote=up)
#             db.session.commit()
#         for downvote in vote:
#             down+=1
#             db.session.add(downvote=down)
#             db.session.commit()
#         user=User.query.filter_by(id = pitch.id).first()
#         return redirect(url_for('.index'))
#
#     return render_template('profile/new_comment.html',comment_form=form)
#     return render_template('new_vote.html',upvote = upvote, downvote = downvote, vote_form=form, votes=votes)

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
