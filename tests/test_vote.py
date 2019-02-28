import unittest
from app.models import Vote,User,Pitch

class VoteModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id=77,name="ttttttttttcfcfghgh",user_id=12345,posted=12/3/2008)
        self.new_vote = Vote(id=77,upvote=23,downvote=45,pitch_id=77)

    # def test_save_vote(self):
    #     self.new_vote.save_vote()
    #     self.assertTrue(len(Vote.query.all())>0)

    def test_get_vote_by_id(self):

        # self.new_vote.save_vote()
        got_votes = Vote.get_votes(77)
        self.assertTrue(len(got_votes) == 0)
