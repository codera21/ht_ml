import random
import unittest
from ht_ml.core.datasets import Datasets


class TestDatasets(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample_data =  'world'
    
    def test_1(self):
        print("hello " + self.sample_data)
        
        
        
if __name__ == '__main__':
    unittest.main()