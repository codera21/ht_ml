from core.datasets import Datasets

def main():
    print("Its do or die situation now")
    d = Datasets('brainyq')
    d.read_dataset()


if __name__ == '__main__':
    main()