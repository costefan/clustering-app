import numpy as np

import random
from collections import defaultdict
import operator


class KMeans:

    def __init__(self, n_clusters: int, max_iterations: int):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations

    def _has_converged(self, old_centers, new_centers) -> bool:

        return set([tuple(a) for a in new_centers])\
               == set([tuple(a) for a in old_centers])

    @staticmethod
    def _group_to_clusters(centers: list, points) -> dict:
        """Group points to clusters
        :param centers: 
        :param points: 
        :return: dictionary, where key - cluster index, value - points in cl
        """
        clusters_dict = defaultdict(list)

        for point in points:
            cluster, min_distance = min(
                [(ix, np.linalg.norm(np.array(point) - np.array(center)))
                 for ix, center in enumerate(centers)], key=lambda x: x[1]
            )
            clusters_dict[cluster].append(point)

        return clusters_dict

    def _reevaluate_centers(self, clusters):
        ordered_clusters = sorted(clusters.items(), key=operator.itemgetter(0))

        return [np.mean(value, axis=0) for _, value in ordered_clusters]

    def fit_predict(self, points: list) -> dict:
        old_centers = random.sample(points, self.n_clusters)
        new_centers = random.sample(points, self.n_clusters)

        iteration = 0
        while not self._has_converged(old_centers, new_centers)\
                and iteration < self.max_iterations:
            old_centers = new_centers

            clusters = self._group_to_clusters(old_centers, points)

            new_centers = self._reevaluate_centers(clusters)
            iteration += 1

        return clusters
