## Creating Dataset

We can create our own custom dataset to generate fake identity cards for testing purpose.

__Class Dataset__ in creating_dataset.py allows multiple parameters for same.
1. profile_img_path :- All fake images for profile photos will be downloaded here.
2. template_image_path :- Image path tha  denotes Architecture for fake id card 
3. name_start_coordinates :- Starting coordinates from where we will start writing name.
4. address_start_coordinates :- Starting coordinates from where we will start writing address.
5. id_start_coordinates :- Starting coordinates from where we will start writing ID.
6. profile_photo_top_left_coordinates :- Top left coordinates for profile photo
7. profile_photo_bottom_right_coordinates :- Bottom right coordinates for profile photo
8. output_dataset :- The folder path where all fake cards will be saved.
9. font :- Font for name ,id and address 
10. name_font_scale :- Font Scale for name  
11. id_font_scale :- Font Scale for id 
12. address_font_scale :- Font Scale address 
13. font_color :- Colour Scheme for font
14. font_thickness :- Thickness of font
15. start_index_of_image :- Images are stored in img_{number} format sequentially.This parameter denotes the number to start from.

All default values are provided and can be customized as per above parameters.

## Extracting Dataset

__class DataExtraction__ in reading_and_extracting_data.py allows this functionality.

1. Takes files path :- The dataset path from which information is to be extracted.
2. Name of output file :- Path to csv file in which extracted data will be stored.

## Running the programs
To run the above tasks
please look into run.py