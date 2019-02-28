import unittest
from app.models import Vote,User

class VoteModelTest(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_vote = Vote(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )

    def test_save_vote(self):
        self.new_vote.save_vote()
        self.assertTrue(len(Vote.query.all())>0)

    def test_get_vote_by_id(self):

        self.new_vote.save_vote()
        got_votes = Review.get_votes(12345)
        self.assertTrue(len(got_votes) == 1)
