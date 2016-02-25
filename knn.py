# Example of kNN implemented from Scratch in Python

import csv
import random
import math
import operator
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from datetime import datetime, timedelta

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(1, len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

	return trainingSet, testSet

def loadFullDataset(filename):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    return list(lines)

def prepareDataset(dataset, split, trainingSet=[], testSet=[]):
    for x in range(1, len(dataset)-1):
        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
        if random.random() < split:
            trainingSet.append(dataset[x])
        else:
            testSet.append(dataset[x])
    # print trainingSet, testSet
    return trainingSet, testSet

def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))

	
	# print distances	
	distances.sort(key=operator.itemgetter(1))


	for x in range(k):
		yield distances[x][0]


def getResponse(neighbors):
	classVotes = {}
	for nb in neighbors:
		response = nb[-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1			
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def _getAccuracies(testSet, predictions):
	for x, tset in enumerate(testSet):
		if tset[-1] == predictions[x]:
			yield 1.0
		else:
			yield 0.0

def getAccuracies(testSet, predictions):
	return sum(_getAccuracies(testSet, predictions))/len(testSet) * 100.0

def getAccuraciesNP(testSet, predictions):
	return np.array(list(_getAccuracies(testSet, predictions))).mean() * 100

	
def main():

	dataset = loadFullDataset('iris.csv')

	for inter in range(1,1000):
		split = float(inter)/100
		# prepare data
		lenTrainingSet = []
		predictions = []
		repetitions = 10	
		for rep in xrange(repetitions):
			print split
			trainingSet, testSet = prepareDataset(dataset, split)
			lenTrainingSet.append(len(trainingSet))
			k = 3
			for testElem in testSet:
				neighbors = getNeighbors(trainingSet, testElem, k)
				predictions.append(getResponse(neighbors))

			# then = datetime.utcnow()
			accuracy = getAccuracies(testSet, predictions)
			# acc1 = datetime.utcnow()-then
			print('Accuracy: ' + repr(accuracy) + '%'),
			# then = datetime.utcnow()
			# print getAccuraciesNP(testSet, predictions)
			# acc2 = datetime.utcnow()-then
			# print acc1, acc2
			print "Thres: {0}, Latest Len Training set: {1}".format(split, lenTrainingSet)
	
main()