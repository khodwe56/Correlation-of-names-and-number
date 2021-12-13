import cv2
import pytesseract
from pytesseract import Output
import glob
import pandas as pd
import logging

class DataExtraction:
    def extract_data(self, files_path="dataset", output_filename="output.csv"):
        paths = glob.glob(files_path + "/*")
        name_to_identity_map = {}
        cnt = 0
        for path in paths:
            if cnt%50:
                logging.info("{} images created successfully.".format(i))
            cnt += 1
            if "diff" in path:
                continue

            img = cv2.imread(path)
            try:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            except FileNotFoundError:
                logging.error("File Not Found {}".format(path))
                exit(0)
            d = None
            try:
                d = pytesseract.image_to_string(img)
            except FileNotFoundError:
                logging.error("Tesseract not in path or not installed properly.")
                exit(0)
            d = d.split("\n")
            name = []
            identity = []
            for i in d:
                if i == "":
                    continue
                else:
                    if "Name:" in i:
                        ans = i.split(":")
                        name.append(ans[1].strip())
                    elif "Id:" in i:
                        ans = i.split(":")
                        identity.append(ans[1].strip())
            for i in range(len(identity)):
                name_to_identity_map[identity[i]] = name[i]
        df = pd.DataFrame(list(name_to_identity_map.items()))
        df.columns = ["ID","NAME"]
        df.to_csv(output_filename,index=False)