import os
import random
from faker import Faker
import requests
import shutil
import cv2
import glob

class Dataset:
    def __init__(self, number_of_ids):
        self.number_of_ids = number_of_ids

    def create_fake_data(self,profile_img_path = "profiles",template_image_path = "templates",name_start_coordinates = (516, 336),address_start_coordinates = (554, 502),id_start_coordinates = (466, 421),profile_photo_top_left_coordinates = (),profile_photo_bottom_right_coordinates = (),output_dataset = "dataset",font = cv2.FONT_HERSHEY_PLAIN,name_font_scale = 2,id_font_scale = 2,address_font_scale = 2,font_color = (0, 0, 255),font_thickness = 1):
        if not os.path.exists(profile_img_path):
            os.mkdir(profile_img_path)
        if not os.path.exists(output_dataset):
            os.mkdir(output_dataset)
        if not os.path.exists(template_image_path) and len(glob.glob(template_image_path+"/*")) < 1:
            print("You should have a template folder with template image named img.png in it.")
            exit(0)
        fake = Faker()
        names = []
        addresses = []
        ids = []
        memory = {0: True}
        for i in range(self.number_of_ids):
            name = fake.name()
            address = fake.address()
            id = 0
            while id in memory:
                id = random.randint(100000000000, 999999999999)
            memory[id] = True
            id = str(id)
            res = ""
            for j in range(12):
                if j != 0 and j % 4 == 0:
                    res += " " + id[j]
                else:
                    res += id[j]
            names.append(name)
            addresses.append(address.split(",")[0])
            ids.append(res)

            if not os.path.exists(profile_img_path + '/img_{}.png'.format(i)):
                r = requests.get("https://thispersondoesnotexist.com/image", stream=True)
                with open(profile_img_path + '/img_{}.png'.format(i), 'wb') as out_file:
                    shutil.copyfileobj(r.raw, out_file)
                del r
        for i in range(self.number_of_ids):
            profile = cv2.imread(profile_img_path + "/img_{}.png".format(i))
            profile = cv2.resize(profile, (profile_photo_bottom_right_coordinates[0] - profile_photo_top_left_coordinates[0], profile_photo_bottom_right_coordinates[1] - profile_photo_top_left_coordinates[1]))
            img = cv2.imread(template_image_path + "/img.png")
            img[profile_photo_top_left_coordinates[1]:profile_photo_bottom_right_coordinates[1], profile_photo_top_left_coordinates[0]:profile_photo_bottom_right_coordinates[0]] = profile
            font = font
            color = font_color
            cv2.putText(img, text=names[i], org=name_start_coordinates, fontFace=font, fontScale=name_font_scale, color=color, thickness=font_thickness)
            cv2.putText(img, text=ids[i], org=id_start_coordinates, fontFace=font, fontScale=id_font_scale, color=color, thickness=font_thickness)
            cv2.putText(img, text=addresses[i], org=address_start_coordinates, fontFace=font, fontScale=address_font_scale, color=color, thickness=font_thickness)
            cv2.imwrite(output_dataset + "/img_{}.png".format(i), img)


NUMBER_OF_IDS = 200


def main():
    fake = Faker()
    names = []
    addresses = []
    ids = []
    memory = {}
    for i in range(NUMBER_OF_IDS):
        name = fake.name()
        address = fake.address()
        id = random.randint(100000000000, 999999999999)
        id = str(id)
        res = ""
        for j in range(12):
            if j != 0 and j % 4 == 0:
                res += " " + id[j]
            else:
                res += id[j]
        names.append(name)
        addresses.append(address.split(",")[0])
        ids.append(res)

        if not os.path.exists('profiles/img_{}.png'.format(i)):
            r = requests.get("https://thispersondoesnotexist.com/image", stream=True)
            with open('profiles/img_{}.png'.format(i), 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
            del r

    # 35,245
    # 389,602
    for i in range(200):
        profile = cv2.imread("profiles/img_{}.png".format(i))
        profile = cv2.resize(profile, (389 - 35, 602 - 245))
        img = cv2.imread("templates/img.png")
        img[245:602, 35:389] = profile
        font = cv2.FONT_HERSHEY_PLAIN
        color = (0, 0, 255)
        cv2.putText(img, text=names[i], org=(516, 336), fontFace=font, fontScale=2, color=color, thickness=1)
        cv2.putText(img, text=ids[i], org=(466, 421), fontFace=font, fontScale=2, color=color, thickness=1)
        cv2.putText(img, text=addresses[i], org=(554, 502), fontFace=font, fontScale=1, color=color, thickness=1)
        cv2.imwrite("dataset/img_{}.png".format(i), img)
