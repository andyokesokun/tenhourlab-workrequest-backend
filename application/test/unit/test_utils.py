import application.utils as utils
import unittest
class TestUtils(unittest.TestCase):
    def test_formatTimeDuration(self):
        testCase =[
            ("25.3", "25min 3sec"),
            ("65.40", "1hr 5min 40sec")
        ] 

        for input, output in testCase:
            with self.subTest():
                self.assertEqual(utils.formatDurationTime(input),output, f"input: {input} output{output}") 


if __name__  == '__main__':
    unittest.main()

