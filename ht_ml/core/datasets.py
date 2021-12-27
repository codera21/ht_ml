from pathlib import Path
import os

class Datasets:
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name.strip().lower()
        self.dataset_path = f"{str(Path(__file__).parent.parent.parent)}/data/{self.dataset_name}/datasets/default/"

    def read_dataset(self, n=1000, max=None):
        # get first n files from the dataset and return them as a list
        print(os.walk(self.dataset_path))
        print(self.dataset_path)
        # for i in range(n):
        #     with open(self.dataset_file, 'r') as f:
        #         pass
