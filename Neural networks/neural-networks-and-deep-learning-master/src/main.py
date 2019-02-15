import mnist_loader
import os

os.chdir(r'C:\Users\沈恺\OneDrive\mypython\Neural networks\neural-networks-and-deep-learning-master\src')

training_data, validation_data, test_data = \
mnist_loader.load_data_wrapper()

import network

net = network.Network([784,30,10])
net.SGD(list(training_data), 30, 10, 3.0, test_data=list(test_data))