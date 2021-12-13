from creating_dataset import Dataset
from reading_and_extracting_data import DataExtraction


def main():
    ## Creates a dataset
    d  = Dataset(300)
    d.create_fake_data()
    ## Run Data Extraction algorithm
    dea = DataExtraction()
    dea.extract_data(files_path="dataset")


if __name__ == "__main__":
    main()
