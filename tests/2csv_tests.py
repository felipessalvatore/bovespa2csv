import unittest
import os
import shutil
# from contra_qa.text_generation.boolean1_neg import boolean1
# from contra_qa.text_generation.boolean2_S_and import boolean2
# from contra_qa.text_generation.boolean3_NP_and import boolean3
# from contra_qa.text_generation.boolean4_VP_and import boolean4


class ParseDataTest(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        # if os.path.exists("data"):
        #     shutil.rmtree("data")
        pass

    @classmethod
    def setUp(cls):
        pass

    def test_read_file(self):
        self.assertTrue(cond)
