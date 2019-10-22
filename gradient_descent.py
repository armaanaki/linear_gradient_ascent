#!/usr/bin/python

# Course: CS4267
# Student name: Armaan Esfahani 
# Student ID: 000764818
# Assignment #: #3
# Due Date: October 23, 2019
# Signature: A.E. 
# Score: _________________

import pandas
import matplotlib.pyplot as plt
import argparse

# parser arguments to make running the program easier
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="the location of the data file (defaults to dataset.csv)")
parser.add_argument("-slr", "--slopelearnrate", help="learn rate of the slope (defaults to 0.1)")
parser.add_argument("-ilr", "--interceptlearnrate", help="learn rate of the intercept (defaults to 0.0001")
args = parser.parse_args()

# use filename if filename was provided
if args.filename:
    filename = args.filename
else:
    filename = "dataset.csv"

# use slope learn rate if provided
if args.slopelearnrate:
    s_l_rate = float(args.slopelearnrate)
else:
    s_l_rate = 0.0001

# use intercept learn rate if provided
if args.interceptlearnrate:
    i_l_rate = float(args.interceptlearnrate)
else:
    i_l_rate = 0.1

# import the dataset using pandas -- this is to make functions on sets easier.
dataset = pandas.read_csv(filename)
X = dataset.iloc[:, 0]
Y = dataset.iloc[:, 1]

# init the slope, intercept
slope = 0
intercept = 0


# function to determine the direction to adjust a given rate, as required by the PDF
def error_delta(dataset, current):
    return -(2.0/len(dataset)) * sum(dataset - current)

# init variables used for loops
slope_error = 1
intercept_error = 1
count = 0
line = None

while abs(slope_error) > 0.02 or abs(intercept_error) > 0.02:
    # get the current guess of Y
    Y_current = slope * X + intercept

    # get the errors
    slope_error = error_delta(X*Y, X * Y_current)
    intercept_error = error_delta(Y, Y_current)

    # determine the new intercept by finding the delta error of the intercept and applying the learning rate
    intercept = intercept - i_l_rate * intercept_error 

    # determine the new slope by finding the delta error of the slope and applying the learning rate
    slope = slope - s_l_rate * slope_error 
    
    count += 1
    print("Epoch: %d\tSlope Error: %.5f\tIntercept Error: %.5f" % (count, slope_error, intercept_error))

# create a prediciton with our final slope and intercept
Y_pred = slope * X + intercept

# plot the data with 
plt.scatter(X, Y) 
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.show()

# print the final slope and intercept
print ("Slope: %.5f\tIntercept: %.5f" % (slope, intercept))
