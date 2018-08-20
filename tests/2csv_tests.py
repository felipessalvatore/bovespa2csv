import unittest
import os
import copy
from bovespa2csv.util import collum_dict, get_data_as_dict
from bovespa2csv.BovespaParser import BovespaParser


class ParseDataTest(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        if os.path.exists(cls.out_csv):
            os.remove(cls.out_csv)
        if os.path.exists(cls.enco_out_csv):
            os.remove(cls.enco_out_csv)
        if os.path.exists(cls.out_xlsx):
            os.remove(cls.out_xlsx)

    @classmethod
    def setUp(cls):
        cls.path = os.path.join("tests", "toy_data", "example.txt")
        cls.enco_path = os.path.join("tests", "toy_data", "enco_toy.txt")

        cls.out_csv = os.path.join("tests", "test.csv")
        cls.out_xlsx = os.path.join("tests", "test.xlsx")
        cls.enco_out_csv = os.path.join("tests", "enco_test.csv")

    def test_read_each_line_of_file(self):
        info_dict = copy.deepcopy(collum_dict)
        my_dict = get_data_as_dict(self.path, info_dict)
        cond = True
        for c in my_dict.keys():
            cond = cond and 10 == len(my_dict[c])
        self.assertTrue(cond)

    def test_read_and_write2csv(self):
        parser = BovespaParser()
        parser.to_csv(self.path, self.out_csv)
        self.assertTrue(os.path.exists(self.out_csv))

    def test_read_char_with_different_encoding(self):
        parser = BovespaParser()
        parser.to_csv(self.enco_path, self.enco_out_csv)
        self.assertTrue(os.path.exists(self.enco_out_csv))

    def test_read_and_write2xlsx(self):
        parser = BovespaParser()
        parser.to_excel(self.path, self.out_xlsx)
        self.assertTrue(os.path.exists(self.out_xlsx))
