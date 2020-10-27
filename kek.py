import pandas as pd 
import numpy as np
from keras import models, layers
from keras.layers import Dropout
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from keras import backend as K
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from keras import metrics
from keras.models import load_model
import seaborn as sns
import matplotlib.pyplot as plt
import os
from keras import optimizers

sns.set_style("darkgrid")
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"


df = pd.read_csv('feature_list.csv')


features_list = [
'kills',
'deaths',
'doublekills',
'triplekills',
'quadrakills',
'pentakills',
'firstblood',
'teamkpm',
'ckpm',
'firstdragon',
'dragons',
'elementaldrakes',
'infernals',
'mountains',
'clouds',
'oceans',
'elders',
'firstherald',
'heralds',
'firstbaron',
'barons',
'firsttower',
'towers',
'firstmidtower',
'firsttothreetowers',
'inhibitors',
'damagetochampions',
'dpm',
'damagetakenperminute',
'damagemitigatedperminute',
'wardskilled',
'wcpm',
'controlwardsbought',
'visionscore',
'vspm',
'totalgold',
'earnedgold',
'earned_gpm',
'goldspent',
'minionkills',
'monsterkills',
'monsterkillsownjungle',
'monsterkillsenemyjungle',
'cspm',
'goldat10',
'xpat10',
'csat10',
'goldat15',
'xpat15',
'csat15']

target = df.result
features = df[features_list]


train_features, test_features, train_target, test_target = train_test_split(features, target, test_size=0.20, random_state=1)


network = models.Sequential()
network.add(layers.Dense(units=64, activation='relu', input_shape=(len(features.columns),)))
network.add(layers.Dense(units=32, activation='relu'))
network.add(layers.Dense(units=1, activation='sigmoid'))

network.compile(loss='binary_crossentropy', optimizer="Adam", metrics=['accuracy']) 

es = EarlyStopping(monitor='val_loss', mode='min', verbose=2, patience=500)
mc = ModelCheckpoint('best_model.h5', monitor='val_loss', mode='min', verbose=2, save_best_only=True)

history = network.fit(train_features, train_target, 
            epochs=1000, verbose=0, batch_size=128, 
            validation_data=(test_features, test_target), callbacks=[es, mc]) 

saved_model = load_model('best_model.h5')

_, train_acc = saved_model.evaluate(train_features, train_target, verbose=0)
_, test_acc = saved_model.evaluate(test_features, test_target, verbose=0)

print('Train Accuracy: %.3f, Test Accuracy: %.3f' % (train_acc, test_acc))

print('Train Accuracy: %.3f, Test Accuracy: %.3f' % (train_acc, test_acc))

plt.subplots(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.title('Loss after each Epoch')
plt.plot(history.epoch[::10], history.history['loss'][::10], label='Train')
plt.plot(history.epoch[::10], history.history['val_loss'][::10], label='Test')
plt.legend(['Train', 'Test'],loc='upper right', title='Sample', facecolor='white',fancybox=True)
plt.xlabel('Loss')
plt.ylabel('Epochs')

plt.subplot(1, 2, 2)
plt.title('Accuracy after each Epoch')
plt.plot(history.epoch[::10], history.history['acc'][::10], label='Train')
plt.plot(history.epoch[::10], history.history['val_acc'][::10], label='Test')
plt.xlabel('Accuracy')
plt.ylabel('Epochs')
plt.legend(['Train', 'Test'], loc='upper left', title='Sample', facecolor='white', fancybox=True)


plt.savefig('loss_acc.jpg', quality=100)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(test_target, saved_model.predict_classes(test_features)))
print(confusion_matrix(test_target, saved_model.predict_classes(test_features)))

print(r"""\
    
_________ _______  _______    _______          ______ 
\__   __/(  ____ \(       )  (  __   )        / ____ \
   ) (   | (    \/| () () |  | (  )  |       ( (    \/
   | |   | (_____ | || || |  | | /   | _____ | (____  
   | |   (_____  )| |(_)| |  | (/ /) |(_____)|  ___ \ 
   | |         ) || |   | |  |   / | |       | (   ) )
   | |   /\____) || )   ( |  |  (__) |       ( (___) )
   )_(   \_______)|/     \|  (_______)        \_____/ 
                                                      
 _                 _       
( \      |\     /|( \      
| (      | )   ( || (      
| |      | |   | || |      
| |      | |   | || |      
| |      | |   | || |      
| (____/\| (___) || (____/\
(_______/(_______)(_______/
                           
""")