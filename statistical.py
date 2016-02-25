from datetime import datetime, timedelta
from random import random, randint
import math
import numpy as np


def random_curve(n, central=200):
	for _ in xrange(n):
		coef = random()
		if bool(int(coef*100) % 2):
			yield central * ( 1 + coef)
		else:
			yield central * ( coef)

euclidean = lambda x, y: math.sqrt((x - y)**2)


def calculate(central, all_values, desired_accuracy):


	accuracies = []
	deviations = []
	best_deviation = float('inf')
	best_reps = 0
	best_accuracy = 0
	best_mean = central

	for _ in range(len(all_values)):
		reps = _ + 1
		values = all_values[:reps]
		# print "{0} -> {1}".format(central, values)
		mean = np.array(values).mean()
		distance = euclidean(central, mean)
		accuracy = 100.0 * float(central) / float(central+distance)
		accuracies.append(accuracy)
		deviations.append(distance)

		# if accuracy > best_accuracy:
		# 	# print "Found a minimum deviation: {0} -> {1}, for {2} reps".format(best_deviation, distance, reps)
		# 	best_deviation = distance
		# 	best_reps = reps
		# 	best_accuracy = accuracy
		# 	best_mean = mean

		if accuracy >= desired_accuracy: # Already found
			break

	print
	if max(accuracies) < desired_accuracy:
		print "Not enough data"
	else:
		print "Reached"

	print "Minimal deviation: {0}, maximum accuracy {1}, with {2} inputs".format(min(deviations), 
		max(accuracies), accuracies.index(max(accuracies))+1)
	print "Best mean found for {0}: {1}".format(central, best_mean)
	print

def main():

	seed = randint(1500, 15000)
	dataset = sorted(random_curve(100, seed))
	central = dataset[randint(1, len(dataset))]
	desired_accuracy = 95.0

	calculate(central, dataset, desired_accuracy)


if __name__ == '__main__':
	main()