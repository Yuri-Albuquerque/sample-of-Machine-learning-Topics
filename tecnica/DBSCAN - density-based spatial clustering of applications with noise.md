#### Density-based spatial clustering of applications with noise (DBSCAN): 
* does not make assumptions about spherical clusters like k-means, 
* nor does it partition the dataset into hierarchies that require a manual cut-off point. 
As its name implies, density-based clustering assigns cluster labels based on dense regions of points. In DBSCAN, the notion of density is defined as the number of points within a specified radius, ε.

According to the DBSCAN algorithm, a special label is assigned to each example (data point) using
the following criteria:
1. A point is considered **a core point** if at least a specified number (MinPts) of neighboring points fall within the specified radius, ε.
2. A border point is a point that has fewer neighbors than MinPts within $\varepsilon$ , but lies with the ε radius of a core point.
3. All other points that are neither core nor border points are considered **noise points**
![[Pasted image 20231127225512.png]]
After labeling the points as core, border, or noise, the DBSCAN algorithm can be summarized in two simple steps:
1. Form a separate cluster for each core point or connected group of core points. (Core points are connected if they are no farther away than ε.)
2. Assign each border point to the cluster of its corresponding core point.

To get a better understanding of what the result of DBSCAN can look like, before jumping to the implementation, let’s summarize what we have just learned about core points, border points, and noise points in the Figure above.

#### Advantages 
One of the main advantages of using DBSCAN is that: 
1. it does not assume that the clusters have a spherical shape as in k-means. 
2. Furthermore, DBSCAN is different from k-means and hierarchical clustering in that it doesn’t necessarily assign each point to a cluster but is capable of removing noise points.
#### Implementation
For a more illustrative example, let’s create a new dataset of half-moon-shaped structures to compare k-means clustering, hierarchical clustering, and DBSCAN:

``` python
from sklearn.datasets import make_moons
>>> X, y = make_moons(n_samples=200,
	...noise=0.05,
	...random_state=0)
>>> plt.scatter(X[:, 0], X[:, 1])
>>> plt.xlabel('Feature 1')
>>> plt.ylabel('Feature 2')
>>> plt.tight_layout()
>>> plt.show()
```

As you can see in the resulting plot, there are two visible, half-moon-shaped groups consisting of 100 examples (data points) each:
![[Pasted image 20231127230538.png]]
##### Comparison with k-means
using the k-means algorithm and complete linkage clustering to see if one of those
previously discussed clustering algorithms can successfully identify the half-moon shapes as separate clusters. The code is as follows:
```python
>>> f, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
>>> km = KMeans(n_clusters=2,
	...random_state=0)
>>> y_km = km.fit_predict(X)
>>> ax1.scatter(X[y_km == 0, 0],
	...X[y_km == 0, 1],
	...c='lightblue',
	...edgecolor='black',
	...marker='o',
	...s=40,
	...label='cluster 1')
>>> ax1.scatter(X[y_km == 1, 0],
	...X[y_km == 1, 1],
	...c='red',
	...edgecolor='black',
	...marker='s',
	...s=40,
	...label='cluster 2')
>>> ax1.set_title('K-means clustering')
>>> ax1.set_xlabel('Feature 1')
>>> ax1.set_ylabel('Feature 2')
>>> ac = AgglomerativeClustering(n_clusters=2,
	...affinity='euclidean',
	...linkage='complete')
>>> y_ac = ac.fit_predict(X)
>>> ax2.scatter(X[y_ac == 0, 0],
	...X[y_ac == 0, 1],
	...c='lightblue',
	...edgecolor='black',
	...marker='o',
	...s=40,
	...label='Cluster 1')
>>> ax2.scatter(X[y_ac == 1, 0],
	...X[y_ac == 1, 1],
	...c='red',
	...edgecolor='black',
	...marker='s',
	...s=40,
	...label='Cluster 2')
>>> ax2.set_title('Agglomerative clustering')
>>> ax2.set_xlabel('Feature 1')
>>> ax2.set_ylabel('Feature 2')
>>> plt.legend()
>>> plt.tight_layout()
>>> plt.show()
```

we can see that the k-means algorithm was unable to separate the two clusters, and also, the hierarchical clustering algorithm was challenged by those complex shapes:

![[Pasted image 20231127231107.png]]
##### DBSCAN on scikit-learn

DBSCAN algorithm on this dataset to see if it can find the two half-moon-shaped clusters using a density-based approach:
```python
>>> from sklearn.cluster import DBSCAN
>>> db = DBSCAN(eps=0.2,
	...min_samples=5,
	...metric='euclidean')
>>> y_db = db.fit_predict(X)
>>> plt.scatter(X[y_db == 0, 0],
	...X[y_db == 0, 1],
	...c='lightblue',
	...edgecolor='black',
	...marker='o',
	...s=40,
	...label='Cluster 1')
>>> plt.scatter(X[y_db == 1, 0],
	...X[y_db == 1, 1],
	...c='red',
	...edgecolor='black',
	...marker='s',
	...s=40,
	...label='Cluster 2')
>>> plt.xlabel('Feature 1')
>>> plt.ylabel('Feature 2')
>>> plt.legend()
>>> plt.tight_layout()
>>> plt.show()
```

The DBSCAN algorithm can successfully detect the half-moon shapes, which highlights one of the
strengths of DBSCAN—clustering data of arbitrary shapes:

![[Pasted image 20231127231456.png]]
##### Disadvantages of DBSCAN

* With an increasing number of features in our dataset (assuming a fixed number of training examples) the negative effect of the **curse of dimensionality** increases. 
* This is especially a problem if we are using the Euclidean distance metric. 
* However, the problem of the curse of dimensionality is not unique to DBSCAN: 
	* it also affects other clustering algorithms that use the Euclidean distance metric, for example, k-means and hierarchical clustering algorithms. 
* In addition, we have two hyperparameters in DBSCAN (MinPts and ε ) that need to be optimized to yield good clustering results. 
* Finding a good combination of MinPts and ε can be problematic if the density differences in the dataset are relatively large.

