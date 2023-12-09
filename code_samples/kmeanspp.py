import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# KMeans clustering using KMeans++
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0)
cluster_labels = kmeans.fit_predict(X)

# Retrieve cluster centers
centroids = kmeans.cluster_centers_

# Retrieve inertia (within-cluster sum of squares)
inertia = kmeans.inertia_

print(f"Cluster Centers:\n{centroids}")
print(f"Inertia (Within-cluster Sum of Squares): {inertia:.2f}")