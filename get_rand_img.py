import glob
import os
import random
import shutil

path = 'airbus_train_bmp/'

rand = random.random()
rand = rand * 200
rand = rand.__int__()
bateau = False

# Choose folder
if rand >= 100:
    bateau = True
    rand = rand - 100

# Build Path
if bateau: 
    path = path + 'bateau/'
else :
    path = path + 'pas_bateau/'

# Get Image
files = os.listdir(path)
file = files[rand]
file = path + file
print(file)
shutil.copy(file, 'temp.bmp')
