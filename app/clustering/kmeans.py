import operator
import random
from collections import defaultdict

import numpy as np

from app.exceptions import WrongClustersNumberError


class KMeans:

    def __init__(self, n_clusters: int, max_iterations: int):
        """
        :param n_clusters: number of clusters
        :param max_iterations: iterations number
        """
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations

    @staticmethod
    def _has_converged(old_centers, new_centers) -> bool:
        """Check converge by comparing old and new centers of the clusters"""

        return set([tuple(a) for a in new_centers])\
            == set([tuple(a) for a in old_centers])

    @staticmethod
    def _group_to_clusters(centers: list, points) -> dict:
        """Group points to clusters.
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
        """Reevaluate centers of the clusters.
        :param clusters: 
        :return: 
        """
        ordered_clusters = sorted(clusters.items(), key=operator.itemgetter(0))

        return [np.mean(value, axis=0) for _, value in ordered_clusters]

    def validate_params(self, points):
        if len(points) <= self.n_clusters:

            raise WrongClustersNumberError(
                "There is no reason to clusterize"
                " points by {} clusters, please,"
                " provide n_clusters < {}".format(self.n_clusters, len(points))
            )

    def fit_predict(self, points: list) -> dict:
        self.validate_params(points)

        old_centers = random.sample(points, self.n_clusters)
        new_centers = random.sample(points, self.n_clusters)
        clusters = {}

        iteration = 0
        while not self._has_converged(old_centers, new_centers)\
                and iteration < self.max_iterations:
            old_centers = new_centers

            clusters = self._group_to_clusters(old_centers, points)

            new_centers = self._reevaluate_centers(clusters)
            iteration += 1

        return clusters
