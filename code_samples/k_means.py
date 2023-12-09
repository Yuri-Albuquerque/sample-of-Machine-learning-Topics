import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# K-means clustering using KMeans
# Number of clusters is specified by 'n_clusters'
kmeans = KMeans(n_clusters=4, random_state=0)  # Creating a KMeans object with 4 clusters
cluster_labels = kmeans.fit_predict(X)  # Fitting the model and predicting clusters for the data

# Retrieving cluster centers and labels for data points
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualizing the clusters and centroids
plt.figure(figsize=(8, 6))

# Plotting data points with their assigned clusters
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', s=50, edgecolor='k', label='Data Points')

# Plotting cluster centers
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='s', s=200, label='Cluster Centers')

plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()