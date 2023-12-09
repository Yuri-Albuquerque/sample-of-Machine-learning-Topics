import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering

# Generating sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Hierarchical clustering using AgglomerativeClustering
# AgglomerativeClustering performs hierarchical clustering using a bottom-up approach
# Number of clusters is specified by 'n_clusters'
agglomerative_cluster = AgglomerativeClustering(n_clusters=4, linkage='ward')  # 'ward' linkage minimizes variance within clusters
cluster_labels = agglomerative_cluster.fit_predict(X)

# Visualizing the clusters
plt.figure(figsize=(8, 6))

# Plotting data points with their assigned clusters
plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', s=50, edgecolor='k')

plt.title('Hierarchical Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()