import unittest
from katas.do_n_times import do_n_times

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        self.counter = 0

        def inc_counter():
            self.counter += 1

        do_n_times(inc_counter, 3)
        self.assertEqual(self.counter, 3)

    def test_zero_times(self):
        self.counter = 0

        def inc_counter():
            self.counter += 1

        do_n_times(inc_counter, 0)
        self.assertEqual(self.counter, 0)

