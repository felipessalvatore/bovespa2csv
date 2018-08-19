import unittest
import os
import shutil
from bovespa2csv.util import collum_dict, parse_line, get_data_as_dict


class ParseDataTest(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        # if os.path.exists("data"):
        #     shutil.rmtree("data")
        pass

    @classmethod
    def setUp(cls):
        cls.path = os.path.join("tests", "toy_data", "example.txt")

    def test_read_each_line_of_file(self):
        info_dict = collum_dict
        my_dict = get_data_as_dict(self.path, info_dict)
        cond = True
        for c in my_dict.keys():
            cond = cond and 10 == len(my_dict[c])
        self.assertTrue(cond)
