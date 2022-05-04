import glob
import time

import cv2
import numpy as np
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

from load_files.load import Loader
from model.classification import BinaryClassifier
from preprocessing.preprocess import Normalization


def main(configuration):
    folder_path = configuration.get("folder_path")
    data_folder = folder_path.get("prefix") + folder_path.get("username") + folder_path.get("postfix")
    pass


def get_files_list(directory, sub_dir=0):
    if sub_dir == 0:
        directory += "/*"
    elif sub_dir == 1:
        directory += "/brain_bone_window/*"
    elif sub_dir == 2:
        directory += "/brain_window/*"
    elif sub_dir == 3:
        directory += "/max_contrast_window/*"
    elif sub_dir == 4:
        directory += "/subdural_window/*"
    else:
        raise ValueError("Invalid subdirectory")

    full_file_names = glob.glob(directory)
    return [x.split("/")[-1].split(".")[0] for x in full_file_names]


if __name__ == '__main__':
    config = yaml.safe_load(open("conf/conf.yaml"))

    loader = Loader()

    # loader.train_test_split("/Users/sakshisuman12/Desktop/MATH7243_project/unzipped/XN_project/renders/", "")

    USERNAME = "sakshisuman12"
    PROJECT_ROOT_DIR = "/Users/" + USERNAME + "/Desktop/MATH7243_project"
    XN_PROJECT_DIR = PROJECT_ROOT_DIR + "/unzipped/XN_project"
    EPIDURAL_DIR = XN_PROJECT_DIR + "/renders/epidural/"
    INTRAPARENCHYMAL_DIR = XN_PROJECT_DIR + "/renders/intraparenchymal/"
    INTRAVENTRICULAR_DIR = XN_PROJECT_DIR + "/renders/intraventricular/"
    MULTI_DIR = XN_PROJECT_DIR + "/renders/multi/"
    NORMAL_DIR = XN_PROJECT_DIR + "/renders/normal/"
    SUBARACHNOID_DIR = XN_PROJECT_DIR + "/renders/subarachnoid"
    SUBDURAL_DIR = XN_PROJECT_DIR + "/renders/subdural"

    all_dirs = {'epidural': EPIDURAL_DIR,
                'intraparenchymal': INTRAPARENCHYMAL_DIR,
                'intraventricular': INTRAVENTRICULAR_DIR,
                # 'multi': MULTI_DIR,
                'normal': NORMAL_DIR,
                'subarachnoid': SUBARACHNOID_DIR,
                'subdural': SUBDURAL_DIR}
    sub_dirs = [1, 2, 3, 4]

    labels = pd.read_csv("/Users/sakshisuman12/Desktop/MATH7243_project/unzipped/XN_project/hemorrhage-labels.csv")

    # for cls in ["epidural", "intraparenchymal"]:
    #     all_file_names = labels[labels[cls] == 1]["Image"].values
    #     get_file_names = all_dirs[cls]
    #     all_files = {}

    all_files = {}
    for dir_key, directory in all_dirs.items():
        directory_files = []
        for sub_dir in sub_dirs:
            directory_files.append(get_files_list(directory, sub_dir))
        all_files[dir_key] = directory_files

    # for dir_key, files in all_files.items():
    #     first, second, third, fourth = files
    #     hmr_file_names = labels[labels[dir_key] == 1]["Image"].values

    corrupted_images = []

    start_time = time.time()

    for dir_key, files in all_files.items():
        first, second, third, fourth = all_files[dir_key]

        other_keys = list(all_dirs.keys())
        other_keys.remove(dir_key)

        X, y = [], []

        for i, file in enumerate(first):
            full_file_path = "/Users/sakshisuman12/Desktop/MATH7243_project/unzipped/XN_project/renders/epidural" \
                             "/brain_bone_window/" + file + ".jpg"
            image_array = cv2.imread(full_file_path)
            if image_array.shape == (512, 512, 3):
                X.append(image_array)
                y.append(1)
            else:
                corrupted_images.append(full_file_path)
            if i % 1000 == 0:
                print(f"Progressing {i}")

        for i, other_key in enumerate(other_keys):
            first_2, second_2, third_2, fourth_2 = all_files[other_key]
            print(f"folder = {other_key}")
            for j, file in enumerate(first_2):
                full_file_path = "/Users/sakshisuman12/Desktop/MATH7243_project/unzipped/XN_project/renders/" + \
                                 other_key + "/brain_bone_window/" + file + ".jpg"
                image_array = cv2.imread(full_file_path)

                if image_array.shape == (512, 512, 3):
                    X.append(image_array)
                    y.append(0)
                else:
                    corrupted_images.append(full_file_path)

                if j % 10000 == 0:
                    print(f"Progressing {j}")

        X = np.array(X)
        y = np.array(y)

        print(len(corrupted_images))

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

        break

    end_time = time.time()

    print(end_time - start_time)
