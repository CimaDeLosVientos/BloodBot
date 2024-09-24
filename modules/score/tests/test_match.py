import unittest

from modules.score.coach import Coach
from modules.score.match import Match


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.coach_own = Coach("Adri", "-1")
        self.coach_away = Coach("Adri Malo", "-1")
        self.match = Match(0, self.coach_own, self.coach_away)

    def test_ok(self):
        self.match.update_data(self.coach_own.name, 1, 3, 4, 5)
        self.match.update_data(self.coach_away.name, 3, 1, 5, 4)
        self.assertTrue(self.match.is_ok())

    def test_ok_report(self):
        self.match.update_data(self.coach_own.name, 1, 3, 4, 5)
        self.match.update_data(self.coach_away.name, 3, 1, 5, 4)
        self.assertEqual("0,Adri,Adri Malo,1,3,4,5", self.match.get_report_trace())

    def test_not_ok(self):
        self.match.update_data(self.coach_own.name, 1, 4, 4, 5)
        self.match.update_data(self.coach_away.name, 3, 1, 5, 4)
        self.assertFalse(self.match.is_ok())

    def test_not_ok_report(self):
        self.match.update_data(self.coach_own.name, 1, 4, 4, 5)
        self.match.update_data(self.coach_away.name, 3, 1, 5, 4)
        self.assertEqual("ERROR", self.match.get_report_trace())

    def test_not_coach_on_match(self):
        self.assertFalse(self.match.is_coach_on_match("pepe"))


if __name__ == '__main__':
    unittest.main()
