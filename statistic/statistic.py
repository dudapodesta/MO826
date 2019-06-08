import numpy as np
import matplotlib.pyplot as plt
from joblib import load
from sklearn.decomposition import PCA
from xgboost import XGBClassifier

from ML.base import pre_process

if __name__ == "__main__":

    data = pre_process()
    X = data.values[:, :-2]
    Y_age = data.values[:, -2]
    Y_bra = data.values[:, -1]

    importances = []

    ## ENTROPY
    clf = load("../ML/tree.model")
    importances.append(clf.feature_importances_)
    importance_indices = np.argsort(importances[0])[::-1]
    labels = [data.columns[i] for i in importance_indices]

    # Print the feature ranking
    print("Feature ranking in Decision Tree Regressor:")

    for f in range(X.shape[1]):
        print("%d. feature %s (%f)" % (f + 1, labels[f], importances[0][importance_indices[f]]))

    ## PCA
    pca = PCA()
    pca.fit(X)
    res = pca.transform(np.eye(X.shape[1]))
    pca_import = np.sum(res, 1)
    pca_import = pca_import - pca_import.min(axis=0)
    pca_import = pca_import/pca_import.sum(axis=0)
    importances.append(pca_import)

    ## Gradient Boosting
    # fit model on training data
    clf = XGBClassifier()
    clf.fit(X, Y_bra)

    importances.append(clf.feature_importances_)
    importance_indices = np.argsort(importances[2])[::-1]
    labels = [data.columns[i] for i in importance_indices]

    # Print the feature ranking
    print("Feature ranking in XGBoost:")

    for f in range(X.shape[1]):
        print("%d. feature %s (%f)" % (f + 1, labels[f], importances[2][importance_indices[f]]))

    # Plot the feature importances of the forest
    plt.figure()
    plt.title("Tree Feature importances")
    width = 0.27
    list_indices = np.array(range(X.shape[1]))
    entropy =   plt.bar(list_indices - width, importances[0][list_indices], width, color="r")
    xgb =       plt.bar(list_indices, importances[2][list_indices],  width, color="g")
    pca =       plt.bar(list_indices + width, importances[1][list_indices],  width, color="b")
    plt.xticks(range(X.shape[1]), data.columns)
    plt.xticks(rotation=90)
    plt.xlim([-1, X.shape[1]])
    plt.legend((entropy[0], xgb[0], pca[0]), ('Entropy', 'Gradient', 'PCA'))
    plt.show()
