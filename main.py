from creating_dataset import Dataset
from reading_and_extracting_data import DataExtraction

def main():
    # d  = Dataset(300)
    # d.create_fake_data()
    algo = DataExtraction()
    algo.extract_data(files_path="test")

if __name__ == "__main__":
    main()