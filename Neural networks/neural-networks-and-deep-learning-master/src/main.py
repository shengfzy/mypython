import mnist_loader
import os
from pylab import *

os.chdir(r'D:\Git\mypython\Neural networks\neural-networks-and-deep-learning-master\src')

training_data0, validation_data0, test_data0 = \
mnist_loader.load_data_wrapper()

training_data = list(training_data0)
validation_data = list(validation_data0)
test_data = list(test_data0)

import network,network2

'''
net = network.Network([784,30,10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
'''

net1 = network2.Network([784,30,10], cost = network2.CrossEntropyCost)
net1.large_weight_initializer()
[evaluation_cost1, evaluation_accuracy1, training_cost1, training_accuracy1] = \
net1.SGD(training_data,30,10,0.1,
evaluation_data = validation_data, lmbda = 5.0,
monitor_evaluation_cost = False, monitor_evaluation_accuracy = True,
monitor_training_cost = False, monitor_training_accuracy = False)

net2 = network2.Network([784,30,10], cost = network2.CrossEntropyCost)
#net.large_weight_initializer()
[evaluation_cost2, evaluation_accuracy2, training_cost2, training_accuracy2] = \
net2.SGD(training_data,30,10,0.1,
evaluation_data = validation_data, lmbda = 5.0,
monitor_evaluation_cost = False, monitor_evaluation_accuracy = True,
monitor_training_cost = False, monitor_training_accuracy = False)

plot(range(0,30), evaluation_accuracy1)
plot(range(0,30), evaluation_accuracy2)
show()