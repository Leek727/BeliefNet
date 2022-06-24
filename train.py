from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.optimizers import SGD
import math
import numpy as np 
import os
import json

# ------------------------- load training data ----------------------------- 
training_data = []
output = []

# read all data from dir
directory = os.fsencode("dataset")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    # load file
    f = open(f'dataset/{file.decode()}')
    data = json.load(f)
    f.close()

    keypresses = [data['pos'][0]-1920/2,data['pos'][1]-1080/2]
    try:
        ang = math.atan2(keypresses[1],keypresses[0]) * (180/math.pi)
    except:
        pass
    
    ang = int(ang)
    #ang = ang/(180/math.pi)
    #x = 100 * math.cos(ang)
    #y = 100 * math.sin(ang)
    #keypresses = [x+1920/2,y+1080/2]

    # get data and reshape
    training_data.append(data['image'])
    output.append(ang)
    print(ang)


print("Data loaded!")

# ------------------------- create neural network ----------------------------- 
model = Sequential()
# belief_net
model.add(Dense(8000))
model.add(Activation('tanh'))
model.add(Dense(4096))
model.add(Activation('tanh'))
model.add(Dense(8000))
model.add(Activation('tanh'))
model.add(Dense(4096))
model.add(Activation('tanh'))
model.add(Dense(2048))
model.add(Activation('tanh'))
model.add(Dense(2048))
model.add(Activation('tanh'))
model.add(Dense(1024)) 
model.add(Activation('tanh'))
model.add(Dense(1024)) 
model.add(Activation('tanh'))
model.add(Dense(784)) 
model.add(Activation('tanh'))
model.add(Dense(512))
model.add(Activation('tanh'))
model.add(Dense(512))
model.add(Activation('tanh'))
model.add(Dense(256))
model.add(Activation('tanh'))
model.add(Dense(128))
model.add(Activation('tanh'))
model.add(Dense(128))
model.add(Activation('tanh'))
model.add(Dense(64))
model.add(Activation('tanh'))
model.add(Dense(32))
model.add(Activation('tanh'))
model.add(Dense(16))
model.add(Activation('tanh'))
model.add(Dense(8))
model.add(Activation('tanh'))

model.add(Dense(1)) # output layer
model.add(Activation('tanh'))

# ------------------------- train ----------------------------- 
#sgd = SGD(lr=0.1)
model.compile(loss="mse", optimizer="adam")

model.fit(training_data, output, True, epochs=1)

#prediction = model.predict(np.array([[0,0],[0,1],[1,0],[1,1]]))
#print(prediction)

# ------------------------- format and save weights ----------------------------- 
print("Saving weights... ")
np.set_printoptions(threshold=np.inf, suppress=True)
np.savetxt('weight.csv' , model.get_weights() , fmt='%s', delimiter=',')


