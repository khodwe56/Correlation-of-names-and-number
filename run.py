import logging

from creating_dataset import Dataset
from reading_and_extracting_data import DataExtraction
import cv2


def main():
    ## Creates a dataset
    d = Dataset(300)
    d.create_fake_data(profile_img_path="profiles", template_image_path="templates/img.png",
                       name_start_coordinates=(516, 336), address_start_coordinates=(554, 502),
                       id_start_coordinates=(466, 421), profile_photo_top_left_coordinates=(35, 602),
                       profile_photo_bottom_right_coordinates=(245, 389), output_dataset="dataset",
                       font=cv2.FONT_HERSHEY_PLAIN, name_font_scale=2, id_font_scale=2, address_font_scale=2,
                       font_color=(0, 0, 255), font_thickness=1, start_index_of_image=0)

    ## Run Data Extraction algorithm
    dea = DataExtraction()
    dea.extract_data(files_path="dataset", output_filename="output.csv")


if __name__ == "__main__":
    main()
