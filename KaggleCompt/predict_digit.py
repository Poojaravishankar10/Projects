import numpy as np
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt
from scipy.io import loadmat
from lib.util import knnclassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
import tensorflow as tf
from skimage import data
from skimage.transform import rescale, resize, downscale_local_mean, rotate
from keras.layers import Dense, Input
from keras.models import Sequential, Model
from sklearn.neighbors import KNeighborsClassifier


def accuracy(truth, preds):
    correct = np.equal(truth, preds)
    output  = np.divide(np.float(np.sum(correct)), np.size(truth))
    return output

def loaddata(filename):
    """
    Returns xTr,yTr,xTe,yTe
    xTr, xTe are in the form nxd
    yTr, yTe are in the form nx1
    """
    data = loadmat(filename)
    xTr = data["x"]; # load in Training data
    yTr = np.round(data["y"]); # load in Training labels
    return xTr,yTr
xTr, yTr = loaddata('/Users/Pooja/Documents/ML/kaggle/train.mat')
xTr = normalize(xTr)
yTr = np.nonzero(yTr)[1]

xOld = xTr
yOld = yTr
xValid = xTr[3500:]
yValid = yTr[3500:]
xTr = xTr[:3500]
yTr = yTr[:3500]

for i in xTr[:]:
    i = i.reshape(28,28)
    image_rotated1 = rotate(i, 40)  
    image_rotated2 = rotate(i, -40) 
    xTr = np.append(xTr, [image_rotated1.flatten()], axis=0)
    xTr = np.append(xTr, [image_rotated2.flatten()], axis=0)

yTr = np.append(yTr, np.repeat(yTr, 2))

xTe = loadmat('/Users/Pooja/Documents/ML/kaggle/test.mat')['x']


input_img = Input(shape=(784,))


encoded = Dense(64, activation='relu')(input_img)

encoded = Dense(2)(encoded) #keep it linear here.

decoded = Dense(64, activation='relu')(encoded)
decoded = Dense(784, activation = 'sigmoid')(decoded)

autoencoder = Model(input=input_img, output=decoded)

autoencoder.compile(optimizer = "adam", loss = "mse")
autoencoder.fit(xTr, xTr, batch_size = 128,
                nb_epoch = 10, verbose = 3)

xNew = autoencoder.predict(xTr)

xTr = np.append(xTr, xNew, axis=0)
yTr = np.append(yTr, yTr, axis=0)



pca = PCA(n_components=100)
pca.fit(xTr)
xTr = pca.transform(xTr)
xValid = pca.transform(xValid)
xTe = pca.transform(xTe)


neigh = KNeighborsClassifier(n_neighbors=1 , weights='distance', algorithm='auto')
neigh.fit(xTr, yTr) 
yTe = neigh.predict(xValid)
print(accuracy(yValid, yTe))
yTe = neigh.predict(xTe)

np.savetxt("yTe.csv", np.dstack((np.arange(0, yTe.size),yTe))[0],"%d,%d",header="id,digit", delimiter=",")

