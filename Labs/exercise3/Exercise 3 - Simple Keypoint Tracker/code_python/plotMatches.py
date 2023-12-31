import matplotlib.pyplot as plt
import numpy as np


def plotMatches(matches, query_keypoints, database_keypoints):
    query_indices = np.nonzero(matches)[0]
    match_indices = matches[query_indices]

    x_from = query_keypoints[0, query_indices]
    x_to = database_keypoints[0, match_indices]
    y_from = query_keypoints[1, query_indices]
    y_to = database_keypoints[1, match_indices]

    for i in range(x_from.shape[0]):
        plt.plot([y_from[i], y_to[i]], [x_from[i], x_to[i]], 'g-', linewidth=3)
