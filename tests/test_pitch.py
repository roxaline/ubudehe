import unittest
from app.models import Pitch,User

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Review(name="ttttttttttcfcfghgh",user_id=12345,user = self.user_James )

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)
