from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class RPitchForm(FlaskForm):

    name = StringField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CPitchForm(FlaskForm):

    name = StringField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('category',choices=[('P','Rough Cut Projects'),('C','Central pitches'),('R','Round Table pitches')])
    name = StringField('Pitch',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    name = StringField('Comment',validators=[Required()])
    submit = SubmitField('Submit')

class VoteForm(FlaskForm):

    # upvote = StringField('Upvote',validators=[Required()])
    # downvote = TextAreaField('Downvote')
    upvote = SubmitField('Upvote')
    downvote = SubmitField('Downvote')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
