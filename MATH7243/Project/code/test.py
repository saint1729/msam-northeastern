import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    image = cv2.imread("/Users/sakshisuman12/Desktop/MATH7243_project/unzipped/XN_project/"
                       "renders/normal/brain_bone_window/ID_04280250b.jpg")
    print(image.shape)

    plt.imshow(image)
    plt.show()
