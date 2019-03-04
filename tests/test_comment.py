import unittest
from app.models import Comment,User,Pitch

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_wecode = User(id=1,username = 'Juru-10',password = '123', email = 'jurassu10@gmail.com')
        self.new_comment = Comment(id=1,name='Money',pitch_id=1)

    # def test_save_comment(self):
    #     self.new_comment.save_comment()
    #     self.assertTrue(len(Comment.query.all())>0)

    # def test_get_comment_by_id(self):
    #
    #     self.new_comment.save_comment()
    #     got_comments = Comment.get_comments(1)
    #     self.assertTrue(len(got_comments) == 1)
