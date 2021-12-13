import cv2
import pytesseract
import glob
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

class DataExtraction:
    def extract_data(self, files_path="dataset", output_filename="output.csv"):
        paths = glob.glob(files_path + "/*")
        name_to_identity_map = {}
        cnt = 1
        for path in paths:
            if cnt % 50 == 0:
                logging.info("{} images extracted successfully.".format(cnt))
            cnt += 1
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

            for j in range(len(identity)):
                try:
                    name_to_identity_map[identity[j]] = name[j]
                except IndexError:
                    logging.error("Issue with file img_{}".format(path.split("/")[-1].split("_")[-1]))
        df = pd.DataFrame(list(name_to_identity_map.items()))
        df.columns = ["ID", "NAME"]
        df.to_csv(output_filename, index=False)
