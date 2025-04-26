import unittest
from katas.time_me import measure_execution_time, sample_function

class TestTimeMe(unittest.TestCase):
    def test_measure_execution_time_1(self):
        self.assertGreaterEqual(measure_execution_time(lambda: None), 0)

    def test_measure_execution_time_2(self):
        self.assertAlmostEqual(measure_execution_time(sample_function), 500, delta=50) #450-550