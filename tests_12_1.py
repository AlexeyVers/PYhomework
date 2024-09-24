import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        trst_walker = runner.Runner('runner')
        for i in range(10):
            trst_walker.walk()
        self.assertEqual(trst_walker.distance, 50)

    def test_run(self):
        trst_runner = runner.Runner('runner')
        for i in range(10):
            trst_runner.run()
        self.assertEqual(trst_runner.distance, 100)

    def test_challenge (self):
        trst_challenge_run = runner.Runner('runner')
        trst_challenge_walk = runner.Runner('runner')
        for i in range(5):
            trst_challenge_run.walk()
            trst_challenge_walk.run()
        self.assertNotEqual(trst_challenge_run.distance, trst_challenge_walk.distance)
