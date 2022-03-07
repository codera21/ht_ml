import random
import unittest
from unittest.case import skip
from ht_ml.core.datasets import Datasets


class TestDatasets(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        d = Datasets()
        cls.data_set = d.read_dataset(n=50000, suffle=True)
        cls.random_data = random.choice(cls.data_set)

    def test_read_dataset_length(self):
        self.assertEqual(len(self.data_set), 50000)

    def test_read_dataset_keys(self):

        self.assertTrue(self.random_data.keys() == {'req_id', 'url',
                                                    'detail_url', 'qoute', 'author', 'html_chunk'})

    @classmethod
    def tearDownClass(cls) -> None:
        cls.data_set = None
        cls.random_data = None


if __name__ == '__main__':
    unittest.main()
