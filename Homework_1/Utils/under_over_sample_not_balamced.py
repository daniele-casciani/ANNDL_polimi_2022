# In the current folder there is the folder "random".
# In the folder random there are the classes folders with the images. (N.B.: this has to be done after having 
# called the "split" script. This script has often been repeated for training set and then for validation set)
# "size" is the number of images we want to obtain: if the number of images before applying script is more than
# "size", then this script will undersample them (eliminate randomly some of them until we reach the desired
# number, which is "size"). If it is less, it creates copies of some of them randomly selected. Note: the seed
# is equal to the one of the notebook.
# Since only oversample may cause overfitting, and only undersample may cause a lot of waste data, we chose this
# way.
# N.B.: data augmentation is useful to avoid overfitting due to oversample of some classes.
# For the standard oversampling/undersampling, we set: 550 for training, 250 for validation. For a more "pushed"
# version of oversampling/undersampling, we set: 1100 for training, 500 for validation.
# We tried also a more "aggressive" oversampling/undersampling, with 1100 for training and 500 for validation.

import os
from os import listdir
from os.path import isfile, join
import random
import shutil

path = './train'

directory_contents = os.listdir(path)
random.seed(42)
size = 500

for item in directory_contents:
    if not os.path.isfile(os.path.join(path, item)) == True:
        myfiles = [f for f in listdir('./train/'+item) if isfile(join('./train/'+item, f))]
        print(myfiles)
        print(item) 
        if (item == 'Species1' or item == 'Species8'):
            size = 3400
        elif (item == 'Species5' or item == 'Species4'):
            size = 900
        elif (item == 'Species6' or item == 'Species7' or item == 'Species2'):
            size = 600
        else:
            size = 700
        if(len(myfiles)) > size:
            for l in range(len(myfiles)-size):
                myfiles = [f for f in listdir('./train/'+item+'/') if isfile(join('./train/'+item+'/', f))]
                i = random.randint(0,len(myfiles)-1)

                print(i)
                os.remove("./train/"+item+'/'+myfiles[i])
                # shutil.copy2('./random/'+myfiles[i],'./random/'+str(l)+'_'+myfiles[i])
        else:
            for l in range(size-len(myfiles)):
                print(item)
                myfiles = [f for f in listdir('./train/'+item+'/') if isfile(join('./train/'+item+'/', f))]
                i = random.randint(0,len(myfiles)-1)
                print(i)
                #os.remove("./random/"+myfiles[i])
                shutil.copy2('./train/'+item+'/'+myfiles[i],'./train/'+item+'/'+str(l)+'_'+myfiles[i])
