import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from skimage.feature import hog

#add your folder name here and place it with main.py
cl = ['Cat','Dog']

#Extracting features and labels from images
def read_image():
    i=0
    imgf=[]
    lab=[]
    for ct in cl:
        for img in os.listdir(ct):
            cim = os.path.join(ct,img)
            img = cv2.imread(cim, cv2.IMREAD_GRAYSCALE)
            img=cv2.resize(img,(64,64))

            #if hog used then no need for reshape hog helps in feature extraction from images
            hog_features = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualize=False)
            imgf.append(hog_features)
            lab.append(ct)
    return np.array(imgf),np.array(lab)

imgn,lab = read_image()

#80%-20% train test split ratio 
xtrain,xtest,ytrain,ytest = train_test_split(imgn,lab,test_size=0.2)

#training model change C to adjust margin to get more accurate result, same with scaling and kernal change it also 
reg = SVC(kernel='rbf', C=1, gamma='scale')
reg.fit(xtrain,ytrain)

o_t_img = cv2.imread("Cat/cat_104.jpg", cv2.IMREAD_GRAYSCALE)
t_img=cv2.resize(o_t_img,(64,64))

#Give an image path here
hog_features = hog(t_img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualize=False)
print(f"The image is of a :{reg.predict(np.array([hog_features]))[0]}")
cv2.imshow("image",o_t_img)
cv2.waitKey(7000)
 