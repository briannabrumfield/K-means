"""
K - Means / Lloyd Algorithm for 3 Clusters v1 
Brianna Brumfield - CS4593

"""

import math
from random import randint

#distance formula
def distance (p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#find Min Distance for each point from centroid and put each element into 
#it's cluster 
def clusters(P, c1, c2, c3):
	#Clusters 
	Cluster1 = []
	Cluster2 = []
	Cluster3 = []
	for i in P:
		d1 = distance(i, c1) #distance from i to centroid 1
		d2 = distance(i, c2) #distance from i to centroid 2
		d3 = distance(i, c3) #distance from i to centroid 3
	
		min_d = min(d1, d2, d3); #minimum distance from i to all centroids

		#put i into its proper cluster
		if min_d == d1:
			Cluster1.append(i)
		elif min_d == d2: 
			Cluster2.append(i)
		elif min_d == d3:
			Cluster3.append(i)

	Clusters = [Cluster1, Cluster2, Cluster3]
	return Clusters


"""
This function will find the average of the clusters and 
the average will be the new centroid
"""
def cluster_avg(Clusters):

	new_centroids = []
	for cluster in Clusters:
		sum_x = 0
		sum_y = 0
		
		for i in cluster:
			sum_x += i[0]
			sum_y += i[1]

		x_avg = sum_x/len(cluster)
		y_avg = sum_y/len(cluster)
		
		centroid = [x_avg, y_avg]
		new_centroids.append(centroid)

	return new_centroids



"""
Main Prog
"""
"""
Initalize all points and centroids

Initialize the centroids at random from the data set
rather than initializing at random from the set range.
Prevent 2 random points from appearing twice ***

"""

#Points
A1 = [2, 10]
A2 = [2, 5]
A3 = [8, 4]
A4 = [5, 8]
A5 = [7, 5]
A6 = [6, 4]
A7 = [1, 2]
A8 = [4, 9]

#Data Set

P = [A1, A2, A3, A4, A5, A6, A7, A8]
print("Data Points:")
for p in P:
	print(p)
print("\n")

#Centroids
c1 = P[randint(0,7)] #centroid 1

c2 = P[randint(0,7)] #centroid 2
while c2 == c1:
	c2 = P[randint(0,7)]

c3 = P[randint(0,7)] #centroid 3
while c3 == c2 or c3 == c1:
	c3 = P[randint(0,7)]

#Initial Centroids
init_centroids = [c1, c2, c3]

#fist we must initialize our clusters
Clusters = clusters(P, c1, c2, c3)

print("Initial Clusters:")
for cluster in Clusters:
	print(cluster)
print("\n")

# First iteration, find updated centroids

newC = cluster_avg(Clusters)
newClusters = clusters(P, newC[0], newC[1], newC[2])

while newClusters != Clusters:
	Clusters = newClusters
	newC = cluster_avg(Clusters)
	newClusters = clusters(P, newC[0], newC[1], newC[2])	

for c in Clusters:
	i = 0
	for p in c:
		i+=1
	if i == 1:
		print("Initial Centroids not good enough. Please try again.")
		quit()

print("Final Clusters:")
for cluster in newClusters:
	print(cluster)
print("\n")

