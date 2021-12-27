from pathlib import Path
import os
import random
import json


class Datasets:
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name.strip().lower()
        self.dataset_path = f"{str(Path(__file__).parent.parent.parent)}/data/{self.dataset_name}/datasets/default/"

        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError(f"Dataset {self.dataset_name} not found")

    def read_dataset(self, n=None, suffle=False):
        # get first n files from the dataset and return them as a list
        datasets = []
        for roots, dir, files in os.walk(self.dataset_path):
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
            file_number = file_number.zfill(9)

            with open(f"{self.dataset_path}/{file_number}.json", 'r') as f:
                str_obj = json.loads(f.read())
                datasets.append(str_obj)
            
        return datasets
