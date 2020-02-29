

import pandas as pd
from collections import Counter
from sklearn.cluster import DBSCAN 

galaxyInfo = pd.read_excel("galaxy.xlsx")

dbScan = DBSCAN(eps = 0.2, min_samples = 10, metric = 'euclidean').fit(galaxyInfo)
labels = dbScan.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

n_noise_ = list(labels).count(-1)


print('Estimated number of clusters: %d' % n_clusters_)
print(Counter(dbScan.labels_))


print('Estimated number of noise: %d' % n_noise_)

