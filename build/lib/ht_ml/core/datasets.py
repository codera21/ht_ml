from ht_ml.constants import DATASET_DIR
import os
import random
import json


class Datasets:

    def read_dataset(self, n=None, suffle=False):

        datasets = []
        max = None
        for roots, dir, files in os.walk(DATASET_DIR):
            if n is None:
                n = len(files) - 2  # -2 because of . and ..

            max = len(files) - 2

        processed = []
        for i in range(n):
            if suffle == True:
                file_number = random.randint(1, max)
                while file_number in processed:
                    file_number = random.randint(1, max)
                processed.append(file_number)
            else:
                file_number = i + 1  # +1 because filename starts with 1

            file_number = str(file_number)
            file_name = f'{file_number.zfill(9)}.json'

            with open(DATASET_DIR / file_name, 'r') as f:
                str_obj = json.loads(f.read())
                if(str_obj['author'] != '' and str_obj['qoute'] != ''):
                    datasets.append(str_obj)

        return datasets
