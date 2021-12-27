
class Datasets: 
    def __init__(self, dataset_name) -> None:
        self.dataset_name = dataset_name.strip().lower()
        self.dataset_file =  f'../../data/{dataset_name}/datasets'
    
    
    def read_dataset(self, n= 1000):
        # get first n files from the dataset and return them as a list
        for i in range(n):
            with open(self.dataset_file, 'r') as f:
                pass