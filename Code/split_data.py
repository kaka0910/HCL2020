import numpy as np
import random
import csv
import os

data_path = "../new/"

def load(file):
        return np.load(file)['arr_0']

def split_data(path, n):

        x_train = []
        y_train = []
        x_test = []
        y_test = []

        for file in os.listdir(path):
            count = 0
            label = int(os.path.splitext(file)[0])
            data = load(path + file)
            all_set = [i for i in range(data.shape[0])]
            test_set = random.sample(all_set, 535)
            train_set = [k for k in all_set if k not in test_set]
            random.shuffle(train_set)
            train = data[train_set, :-1]
            test = data[test_set, :-1]

            for i in range(0, len(train_set)-n+1, n):
                x_train.append(train[i:i+n].tolist())
                y_train.append(label)
                print("author: ", label, " shape of x_train: ", len(x_train), " ", len(x_train[-1]), " ", len(x_train[-1][0])," shape of y_train: ", len(y_train))
            for j in range(0, len(test_set)-n+1, n):
                x_test.append(test[j:j+n].tolist())
                y_test.append(label)
                print("author: ", label, " shape of x_train: ", len(x_test), " ", len(x_test[-1]), " ", len(x_test[-1][0]), " shape of y_test: ", len(y_test))



        x_train = np.array(x_train).astype(np.uint8)
        x_test = np.array(x_test).astype(np.uint8)	
        y_train = np.array(y_train).astype(np.uint16)
        y_test = np.array(y_test).astype(np.uint16)
        print("train's shape: ", x_train.shape, y_train.shape)
        print("test's shape: ", x_test.shape, y_test.shape)
        np.savez("1000_x_train.npz", x_train)
        np.savez("1000_y_train.npz", y_train)
        np.savez("1000_x_test.npz", x_test)
        np.savez("1000_y_test.npz", y_test)

def split_data_2(path):

        x_train = []
        y_train = []
        x_test = []
        y_test = []

        for file in os.listdir(path):
            author = int(os.path.splitext(file)[0])
            print("author: ", author)
            data = load(path + file)
            all_set = [i for i in range(data.shape[0])]
            test_set = random.sample(all_set, 545)
            train_set = [k for k in all_set if k not in test_set]
            random.shuffle(train_set)
            x_train.extend(data[train_set, :-1].tolist())
            y_train.extend(data[train_set, -1].tolist())
            x_test.extend(data[test_set, :-1].tolist())
            y_test.extend(data[test_set, -1].tolist())
            print("3755 train shape: ", len(x_train), len(y_train))
            print("3755 test shape: ", len(x_test), len(y_test))

        x_train = np.array(x_train).astype(np.uint8)
        x_test = np.array(x_test).astype(np.uint8)	
        y_train = np.array(y_train).astype(np.uint16)
        y_test = np.array(y_test).astype(np.uint16)
        print("train's shape: ", x_train.shape, y_train.shape)
        print("test's shape: ", x_test.shape, y_test.shape)
        np.savez("3755_x_train.npz", x_train)
        np.savez("3755_y_train.npz", y_train)
        np.savez("3755_x_test.npz", x_test)
        np.savez("3755_y_test.npz", y_test)

def rotate_180(file):
        x = load(file)
        print("loaded ", file, ", file shape: ", x.shape)

        y = np.array([np.concatenate((k, k[::-1]), axis=0) for k in x])
        print("shape of y: ", y.shape)

        np.savez("180-2same-" + file, y)

def square(path):
	
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        for file in os.listdir(path):
            count = 0
            label = int(os.path.splitext(file)[0])
            data = load(path + file)
            all_set = [i for i in range(data.shape[0])]
            test_set = random.sample(all_set, 535)
            train_set = [k for k in all_set if k not in test_set]
            random.shuffle(train_set)
            train = data[train_set, :-1]
            test = data[test_set, :-1]

            for i in range(0, len(train_set)-4+1, 4):
                a = train[i:i+2].reshape(56,28)
                b = train[i+2:i+4].reshape(56,28)
                c = np.concatenate((a, b), axis=1)
                x_train.append(c)
                y_train.append(label)
                #print("author: ", label, " shape of x_train: ", len(x_train), " ", x_train[-1].shape, " shape of y_train: ", len(y_train))
            for j in range(0, len(test_set)-4+1, 4):
                a = test[j:j+2].reshape(56,28)
                b = test[j+2:j+4].reshape(56,28)
                c = np.concatenate((a, b), axis=1)
                x_test.append(c)
                y_test.append(label)


            print("author: ", label, " shape of x_train: ",len(x_train)," test: ", len(x_test), " shape: ", x_test[-1].shape, " shape of y_train: ",len(y_train)," test: ", len(y_test))


        x_train = np.array(x_train).astype(np.uint8)
        x_test = np.array(x_test).astype(np.uint8)	
        y_train = np.array(y_train).astype(np.uint16)
        y_test = np.array(y_test).astype(np.uint16)
        print("train's shape: ", x_train.shape, y_train.shape)
        print("test's shape: ", x_test.shape, y_test.shape)
        np.savez("square_x_train.npz", x_train)
        np.savez("square_y_train.npz", y_train)
        np.savez("square_x_test.npz", x_test)
        np.savez("square_y_test.npz", y_test)

def get_badcase():
	
        a = set()
        with open("badcase.csv","r") as cf:
                reader = csv.reader(cf)
                for item in reader:
                    a.add(int(item[0]))

        a = list(a)
        print(len(a))
        print(a[0], type(a[0]))	
        x = []
        y = []

        for file in os.listdir(data_path):
            data = load(data_path + file)
            for row in data:
                key  = row[-1]
                #print(key, type(key))
                if key in a:
                    x.append(row[:-1])
                    y.append(key)	

            print("author: ", os.path.splitext(file)[0], " shape of x: ", len(x), " ", x[-1].shape, " shape of y: ", len(y))
            break

        x = np.array(x).astype(np.uint8)
        y = np.array(y).astype(np.uint16)
        print("train's shape: ", x.shape, y.shape)
        np.savez("badcase_x.npz", x)
        np.savez("badcase_y.npz", y)


get_badcase()

