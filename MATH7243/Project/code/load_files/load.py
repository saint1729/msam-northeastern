import cv2
import numpy as np
from sklearn.model_selection import train_test_split


class Loader:

    def load(self, path):
        """

        :param path:
        :return: numpy array after loading the RGB values
        """
        return cv2.imread(path)

    def load_file_paths(self, folder, classes, class_name, labels, shade):
        """

        :param class_name:
        :param classes:
        :param folder:
        :param labels:
        :param shade:
        :return: X_train and Y_train
        """

        # positives = labels[labels[class_] == 1]["Image"]
        # negatives = labels[labels[class_] == 0]["Image"]

        # folder = folder + "/" + class_ + "/" + shade + "/"

        # X = np.array([self.load(folder + "/" + classes[label[class_name]]) for label in labels])
        # y = np.append(np.ones((positives.shape[0], 1)), np.zeros((negatives.shape[0], 1), axis=0))
        #
        # return X, y[:, 0]
        pass

    def train_test_split(self, folder, class_, labels, shade):
        # X, y = self.load_file_paths(folder, class_, labels, shade)
        # return train_test_split(X, y, test_size=0.2, random_state=42)
        pass
