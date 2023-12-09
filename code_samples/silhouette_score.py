import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Calculate silhouette score for different values of k
for k in range(2, 7):  # Testing for k values from 2 to 6
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=0)
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(f"For n_clusters = {k}, the average silhouette score is : {silhouette_avg:.3f}")