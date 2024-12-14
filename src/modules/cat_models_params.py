from sklearn.ensemble import (
    AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier,
    HistGradientBoostingClassifier, RandomForestClassifier, VotingClassifier, StackingClassifier
)
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.naive_bayes import BernoulliNB, CategoricalNB, ComplementNB, GaussianNB, MultinomialNB
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.linear_model import (
    LogisticRegression, LogisticRegressionCV, RidgeClassifier, RidgeClassifierCV,
    SGDClassifier, PassiveAggressiveClassifier, Perceptron
)
from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier, NearestCentroid
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.multioutput import ClassifierChain, MultiOutputClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.dummy import DummyClassifier
from sklearn.semi_supervised import LabelPropagation, LabelSpreading
from sklearn.neural_network import MLPClassifier

cat_param_grid = {
    "AdaBoostClassifier": {
        "model": AdaBoostClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 1.0],
            "algorithm": ["SAMME", "SAMME.R"]
        }
    },
    "BaggingClassifier": {
        "model": BaggingClassifier(),
        "params": {
            "n_estimators": [10, 50, 100],
            "max_samples": [0.5, 1.0],
            "max_features": [0.5, 1.0],
            "bootstrap": [True, False]
        }
    },
    "BernoulliNB": {
        "model": BernoulliNB(),
        "params": {
            "alpha": [0.1, 1.0, 10.0],
            "fit_prior": [True, False]
        }
    },
    "CalibratedClassifierCV": {
        "model": CalibratedClassifierCV(),
        "params": {
            "cv": [3, 5],
            "method": ["sigmoid", "isotonic"]
        }
    },
    "CategoricalNB": {
        "model": CategoricalNB(),
        "params": {
            "alpha": [0.1, 1.0, 10.0],
            "fit_prior": [True, False]
        }
    },
    "ComplementNB": {
        "model": ComplementNB(),
        "params": {
            "alpha": [0.1, 1.0, 10.0],
            "fit_prior": [True, False]
        }
    },
    "DecisionTreeClassifier": {
        "model": DecisionTreeClassifier(),
        "params": {
            "criterion": ["gini", "entropy"],
            "max_depth": [None, 10, 20, 30],
            "min_samples_split": [2, 5, 10]
        }
    },
    "DummyClassifier": {
        "model": DummyClassifier(),
        "params": {
            "strategy": ["stratified", "most_frequent", "prior", "uniform"],
        }
    },
    "ExtraTreeClassifier": {
        "model": ExtraTreeClassifier(),
        "params": {
            "criterion": ["gini", "entropy"],
            "splitter": ["best", "random"],
            "max_depth": [None, 10, 20]
        }
    },
    "ExtraTreesClassifier": {
        "model": ExtraTreesClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],
            "criterion": ["gini", "entropy"],
            "max_features": ["sqrt", "log2"]
        }
    },
    "GaussianNB": {
        "model": GaussianNB(),
        "params": {}
    },
    "GaussianProcessClassifier": {
        "model": GaussianProcessClassifier(),
        "params": {
            "max_iter_predict": [100, 200],
            "multi_class": ["one_vs_rest", "one_vs_one"]
        }
    },
    "GradientBoostingClassifier": {
        "model": GradientBoostingClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 1.0],
            "max_depth": [3, 5, 10]
        }
    },
    "HistGradientBoostingClassifier": {
        "model": HistGradientBoostingClassifier(),
        "params": {
            "learning_rate": [0.01, 0.1, 0.5],
            "max_iter": [100, 200],
            "max_depth": [None, 10, 20]
        }
    },
    "KNeighborsClassifier": {
        "model": KNeighborsClassifier(),
        "params": {
            "n_neighbors": [3, 5, 7],
            "weights": ["uniform", "distance"],
            "algorithm": ["auto", "ball_tree", "kd_tree", "brute"]
        }
    },
    "LinearDiscriminantAnalysis": {
        "model": LinearDiscriminantAnalysis(),
        "params": {
            "solver": ["svd", "lsqr", "eigen"],
            "shrinkage": [None, "auto"]
        }
    },
    "LinearSVC": {
        "model": LinearSVC(),
        "params": {
            "C": [0.1, 1, 10],
            "loss": ["hinge", "squared_hinge"],
            "max_iter": [1000, 2000]
        }
    },
    "LogisticRegression": {
        "model": LogisticRegression(),
        "params": {
            "C": [0.1, 1, 10],
            "solver": ["liblinear", "lbfgs"],
            "max_iter": [100, 200]
        }
    },
    "MLPClassifier": {
        "model": MLPClassifier(),
        "params": {
            "hidden_layer_sizes": [(50,), (100,), (50, 50)],
            "activation": ["relu", "tanh", "logistic"],
            "solver": ["adam", "sgd"],
            "learning_rate": ["constant", "adaptive"]
        }
    },
    "RandomForestClassifier": {
        "model": RandomForestClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],
            "criterion": ["gini", "entropy"],
            "max_depth": [None, 10, 20],
            "bootstrap": [True, False]
        }
    }
}
