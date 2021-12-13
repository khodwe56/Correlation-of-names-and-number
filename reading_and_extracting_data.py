import cv2
import pytesseract
from pytesseract import Output
import glob
import pandas as pd


class DataExtraction:
    def extract_data(self, files_path="dataset", output_filename="output.csv"):
        paths = glob.glob(files_path + "/*")
        name_to_identity_map = {}
        for path in paths:
            if "diff" in path:
                continue
            img = cv2.imread(path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            d = pytesseract.image_to_string(img)
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