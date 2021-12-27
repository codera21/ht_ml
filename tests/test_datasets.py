import random
import unittest
from unittest.case import skip
from ht_ml.core.datasets import Datasets


class TestDatasets(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        d = Datasets("brainyq")
        cls.data_set = d.read_dataset(n=10, suffle=True)
        cls.random_data = random.choice(cls.data_set)

    def test_dataset_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            d = Datasets('not-bq')
            d.read_dataset()

    def test_read_dataset_length(self):
        self.assertEqual(len(self.data_set), 10)

    def test_read_dataset_obj(self):
        self.assertIsInstance(self.random_data, dict)

    def test_read_dataset_keys(self):
        self.assertTrue(self.random_data.keys() == {'req_id', 'url',
                                                    'detail_url', 'qoute', 'author', 'html_chunk'})


if __name__ == '__main__':
    unittest.main()
