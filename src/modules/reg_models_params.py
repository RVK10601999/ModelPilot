from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet, Lars, LassoLars, OrthogonalMatchingPursuit, 
    BayesianRidge, ARDRegression, HuberRegressor, PassiveAggressiveRegressor, RANSACRegressor, 
    TheilSenRegressor, QuantileRegressor
)

regression_model_params = {
    "LinearRegression": {
        "model": LinearRegression(),
        "params": {
            "fit_intercept": [True, False],
            "normalize": [True, False]
        }
    },
    "Ridge": {
        "model": Ridge(),
        "params": {
            "alpha": [0.1, 1.0, 10.0],
            "fit_intercept": [True, False],
            "solver": ["auto", "svd", "cholesky", "lsqr", "sparse_cg", "sag", "saga"]
        }
    },
    "Lasso": {
        "model": Lasso(),
        "params": {
            "alpha": [0.01, 0.1, 1.0, 10.0],
            "max_iter": [1000, 2000],
            "fit_intercept": [True, False]
        }
    },
    "ElasticNet": {
        "model": ElasticNet(),
        "params": {
            "alpha": [0.01, 0.1, 1.0, 10.0],
            "l1_ratio": [0.2, 0.5, 0.8],
            "fit_intercept": [True, False]
        }
    },
    "Lars": {
        "model": Lars(),
        "params": {
            "n_nonzero_coefs": [500, 1000, 2000],
            "fit_intercept": [True, False],
            "normalize": [True, False]
        }
    },
    "LassoLars": {
        "model": LassoLars(),
        "params": {
            "alpha": [0.01, 0.1, 1.0, 10.0],
            "fit_intercept": [True, False],
            "normalize": [True, False]
        }
    },
    "OrthogonalMatchingPursuit": {
        "model": OrthogonalMatchingPursuit(),
        "params": {
            "n_nonzero_coefs": [None, 5, 10, 15],
            "fit_intercept": [True, False],
            "normalize": [True, False]
        }
    },
    "BayesianRidge": {
        "model": BayesianRidge(),
        "params": {
            "alpha_1": [1e-6, 1e-5, 1e-4],
            "alpha_2": [1e-6, 1e-5, 1e-4],
            "lambda_1": [1e-6, 1e-5, 1e-4],
            "lambda_2": [1e-6, 1e-5, 1e-4]
        }
    },
    "ARDRegression": {
        "model": ARDRegression(),
        "params": {
            "alpha_1": [1e-6, 1e-5, 1e-4],
            "alpha_2": [1e-6, 1e-5, 1e-4],
            "lambda_1": [1e-6, 1e-5, 1e-4],
            "lambda_2": [1e-6, 1e-5, 1e-4]
        }
    },
    "HuberRegressor": {
        "model": HuberRegressor(),
        "params": {
            "epsilon": [1.1, 1.35, 1.5, 1.75],
            "alpha": [0.0001, 0.001, 0.01, 0.1],
            "fit_intercept": [True, False]
        }
    },
    "PassiveAggressiveRegressor": {
        "model": PassiveAggressiveRegressor(),
        "params": {
            "C": [0.01, 0.1, 1.0, 10.0],
            "epsilon": [0.1, 0.5, 1.0],
            "loss": ["epsilon_insensitive", "squared_epsilon_insensitive"],
            "fit_intercept": [True, False]
        }
    },
    "RANSACRegressor": {
        "model": RANSACRegressor(),
        "params": {
            "min_samples": [0.1, 0.5, 0.75],
            "max_trials": [100, 200, 500],
            "stop_probability": [0.95, 0.99]
        }
    },
    "TheilSenRegressor": {
        "model": TheilSenRegressor(),
        "params": {
            "fit_intercept": [True, False],
            "max_subpopulation": [1e4, 1e6, 1e7]
        }
    },
    "QuantileRegressor": {
        "model": QuantileRegressor(),
        "params": {
            "alpha": [0.1, 1.0, 10.0],
            "quantile": [0.1, 0.5, 0.9]
        }
    }
}
