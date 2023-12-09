Yes, your statement is generally correct. In the context of decision trees used for regression tasks:

- **Homogeneity in a Node:** When a decision tree node contains a set of numerical samples that are completely homogeneous (all samples have the same value), it means that there is no variability in those samples.

- **Standard Deviation and Variability:** The standard deviation measures the amount of variation or dispersion in a set of values. If all the values in a set are the same (homogeneous), the standard deviation of that set would indeed be zero.

- **Implications for Decision Trees in Regression:** In the context of decision tree regression, a node that is perfectly homogeneous in terms of the target variable (all samples have the same target value) would indeed have a standard deviation of zero.

- **Impact on Decision Making:** In a decision tree, when a node is completely homogeneous (standard deviation equals zero), it means that no further splitting based on that feature will improve the homogeneity or reduce the variance of the target variable within that node.

This condition of zero standard deviation in a node can influence decision tree algorithms, as they may stop further splitting (or growing) that node if there's no benefit in splitting based on that particular feature.

However, in practice, due to finite precision arithmetic and the nature of real-world data, achieving an exact standard deviation of zero is rare and might not be entirely attainable. Often, numerical values may be very close but not exactly the same, leading to a very small, non-zero standard deviation.