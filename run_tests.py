from app.clustering.kmeans import KMeans

a = [[51.1, 30.2],
    [64.91, 51.67],
    [70.45, 68.7],
    [61.9, 45.2]]

res = KMeans(n_clusters=3, max_iterations=100).fit_predict(a)

print(res)