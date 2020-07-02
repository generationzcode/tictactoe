from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# help from https://stackoverflow.com/questions/27003423/staleelementreferenceexception-on-python-selenium
import keras
from keras.layers import *
from keras import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import sys
sys.setrecursionlimit(100000)

import time
from random import randint
modelx = Sequential()
""""model.add(LSTM(30,input_shape=(predictors.shape[1],predictors.shape[2])))
model.add(Conv2D(30,(1,1),activation="softmax"))
model.summary()
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics = ["accuracy"])"""
modelx.add(LSTM(9, input_shape=(None, 3)))
modelx.add(Dense(1, activation='softmax'))
modelx.compile(loss='MSE', optimizer='sgd')


modely = Sequential()
""""model.add(LSTM(30,input_shape=(predictors.shape[1],predictors.shape[2])))
model.add(Conv2D(30,(1,1),activation="softmax"))
model.summary()
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics = ["accuracy"])"""
modely.add(LSTM(150, input_shape=(None, 3)))
modely.add(RepeatVector(30))
modely.add(LSTM(150))
modely.add(Dense(1, activation='softmax'))
modely.compile(loss='MSLE', optimizer='rmsprop', metrics=['accuracy'])

URL = "https://tictactoe--generationxcode.repl.co/"
clicked = [20]
x_wins = []
y_wins = []
x_log = []
y_log = []
x_y_log =[]
y_y_log= []
all_x_y_log = []
all_y_y_log = []
all_x_log = []
all_y_log = []
game_arr = [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
active_player=True
all_x_wins = []
all_y_wins = []
#true stands for O
winning = ""
time.sleep(3)
def convertWin(arr):
    arr2 = arr
    for i in range(0,len(arr)-1):
        if arr[i][1] == 1:
            arr2[i] = [0,0,1]
        elif arr[i][2] == 1:
            arr2[i] = [0,1,0]
    return arr2

def random_click():
    global active_player
    random_element = randint(0,8)
    checkClicked = False
    for i in clicked:
        if i == random_element:
            random_click()
            checkClicked = True
    if checkClicked == False:
            if active_player == False:
                x_log.append(game_arr)
                game_arr[random_element] = [0,1,0]
                x_y_log.append(random_element)
                active_player = True
                clicked.append(random_element)
                elements[random_element].click()
            else:
                y_log.append(game_arr)
                game_arr[random_element] = [0,0,1]
                y_y_log.append(random_element)
                active_player = False
                clicked.append(random_element)
                elements[random_element].click()
                print(modelx.predict([[game_arr]]))
                
def random_click1():
    global active_player1
    random_element = randint(0,8)
    checkClicked = False
    for i in clicked:
        if i == random_element:
            random_click1()
            checkClicked = True
    if checkClicked == False:
            if active_player1 == False:
                x_log.append(game_arr)
                game_arr[random_element] = [0,1,0]
                x_y_log.append(random_element)
                active_player = True
                clicked.append(random_element)
            else:
                y_log.append(game_arr)
                game_arr[random_element] = [0,0,1]
                y_y_log.append(random_element)
                active_player = False
                clicked.append(random_element)
for v in range(0,100):
    for i in range(0,8):
        if(winner.text == "X"):
            print("x won")
            winning="x"
            break
        elif(winner.text == "O"):
            print("O won")
            winning = "O"
            break
        else:       
            random_click1()      
    print(winning)
    

driver = webdriver.Firefox(executable_path = 'C:/Users/arjun/OneDrive/Documents/geckodriver-v0.26.0-win64/geckodriver.exe')
driver.get(URL)


row1_cell1=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]')
row1_cell2=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]')
row1_cell3=driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[3]')

row2_cell1=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]')
row2_cell2=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]')
row2_cell3=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[3]')

row3_cell1=driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]')
row3_cell2=driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]')
row3_cell3=driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[3]')

winner=driver.find_element_by_xpath('//*[@id="root"]/p/b')
print(winner.text)
elements = [row1_cell1,row1_cell2,row1_cell3,row2_cell1,row2_cell2,row2_cell3,row3_cell1,row3_cell2,row3_cell3]
for v in range(0,100):
    for i in range(0,8):
        if(winner.text == "X"):
            time.sleep(0.5)
            print("x won")
            winning="x"
            break
        elif(winner.text == "O"):
            time.sleep(0.5)
            print("O won")
            winning = "O"
            break
        else:
            time.sleep(0.25)       
            random_click()
    time.sleep(0.5)        
    print(winning)
    print(winner.text)
    print(game_arr)
    if winner.text == "X":
            x_wins = game_arr
            y_wins = game_arr
            for i in range(0,len(game_arr)):
                if game_arr[i][2] == 1:
                    y_wins[i] = [0,1,0]
                elif game_arr[i][1] == 1:
                    y_wins[i] = [0,0,1]
    elif winner.text == "O":
            x_wins = game_arr
            y_wins = game_arr
            for i in range(0,len(game_arr)):
                if game_arr[i][2] == 1:
                    x_wins[i] = [0,1,0]
                elif game_arr[i][1] == 1:
                    x_wins[i] = [0,0,1]



    if winner.text == "X":
        for i in range(0,len(y_log)-1):
            y_log[i] = convertWin(y_log)
            y_y_log = x_y_log
    else:
        for i in range(0,len(x_log)-1):
            x_log[i] = convertWin(x_log)
            x_y_log = y_y_log
    
    all_x_wins.append(x_wins)
    all_y_wins.append(y_wins)
    all_x_y_log.append(x_y_log)
    all_y_y_log.append(y_y_log)
    all_x_log.append(x_log)
    all_y_log.append(y_log)
    modelx.fit([x_log[0]],x_y_log[0],epochs=1)
    print("x_log")
    print(x_log)
    print("y_log")
    print(y_log)
    x_log = []
    y_log = []
    x_y_log =[]
    y_y_log= []
    print(game_arr)
    game_arr = [[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
    clicked = []
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="root"]/button').click()
    print(x_wins)

x_log = []
x_y_log = []
for v in all_x_y_log:
    for i in v:
            x_y_log.append(i)
            
for i in all_x_log:
    for v in i:
        x_log.append(v)
modelx.fit(x_log,x_y_log,epochs=100)
print("cuul")
print(modelx.predict(x_log))
print("very cuul")

