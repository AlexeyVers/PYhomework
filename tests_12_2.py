import unittest
import runner_and_tournament as runner_t

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.setUp = []
        setUp_list = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        for people, speed in setUp_list.items():
            self.setUp.append(runner_t.Runner(people, speed))

    def tearDownClass(self):
        print(self.all_results[0])

    def test_t1(self):
        all_people = runner_t.Tournament(90, self.setUp[0], self.setUp[2])
        self.all_results = all_people.start()
        self.assertEqual(self.all_results[1], self.setUp[2])

    def test_t2(self):
        all_people = runner_t.Tournament(90, self.setUp[1], self.setUp[2])
        self.all_results = all_people.start()
        self.assertEqual(self.all_results[1], self.setUp[2])

    def test_t3(self):
        all_people = runner_t.Tournament(90, *self.setUp)
        self.all_results = all_people.start()
        self.assertEqual(self.all_results[2], self.setUp[2])

