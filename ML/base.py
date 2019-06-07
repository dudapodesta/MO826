import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":

    # making data frame from csv file
    data = pd.read_csv("../data/NACC.csv", index_col="NACCID")

    # print number of columns
    print("Original data set has %d samples and %d variables" % (data.shape[0], data.shape[1]))

    # dropping passed columns
    data.drop(
        ["NACCNEC", "NACCWRI1", "NACCWRI2", "NACCWRI3", "NACCINT", "NACCPICK", "NACCCBD", "NACCPROG", "NACCADC",
         "NACCMOD",
         "NACCYOD", "NACCAUTP", "NPFORMVER"], axis=1, inplace=True)

    # clean data
    data = data.query('NACCBRAA <= 7')

    # print number of columns
    print("After drop data set has %d samples and %d variables" % (data.shape[0], data.shape[1]))

    X = data.values[:, :-2]
    Y_age = data.values[:, -2]
    Y_bra = data.values[:, -1]

    # Split the dataset in two equal parts
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y_bra, test_size=0.5, random_state=0)

    # Set the parameters by cross-validation
    depths = [2, 3, 4, 5, 6, 10, 100, 1000]
    tuned_parameters = [{'max_depth': depths}]
    scores = ['neg_mean_absolute_error', 'neg_mean_squared_error']

    best_index = -1
    best_clf = None
    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print()

        clf = GridSearchCV(tree.DecisionTreeRegressor(), tuned_parameters, cv=5,
                           scoring=score)
        clf.fit(X_train, y_train)

        print("Best parameters set found on development set:")
        print()
        print(clf.best_params_)
        print()
        print("Grid scores on development set:")
        print()
        means = clf.cv_results_['mean_test_score']
        stds = clf.cv_results_['std_test_score']
        for mean, std, params in zip(means, stds, clf.cv_results_['params']):
            print("%0.3f (+/-%0.03f) for %r"
                  % (mean, std * 2, params))
        print()

        # save deepest tree found between estimators
        if clf.best_index_ > best_index:
            best_index = clf.best_index_
            best_clf = clf.best_estimator_

    y_true, y_pred = y_test, best_clf.predict(X_test)
    y_pred_ceil = np.ceil(y_pred).astype(int)  # ceiling melhorou 15% a acc
    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    print(classification_report(y_true, y_pred_ceil))
    print()
    print()

    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax0, ax1 = axes.flatten()
    ax0.hist(y_test, 8, density=True, histtype='bar')
    ax0.set_title('Original')

    ax1.hist(y_pred, 8)
    ax1.set_title('Predicted')

    fig.tight_layout()
    plt.show()
