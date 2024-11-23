import streamlit as st
from models_module import model_utils as mu
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,Lars,LassoLars,OrthogonalMatchingPursuit,BayesianRidge,ARDRegression,HuberRegressor,PassiveAggressiveRegressor,RANSACRegressor,TheilSenRegressor,QuantileRegressor
from sklearn.ensemble._weight_boosting import AdaBoostClassifier
from sklearn.ensemble._bagging import BaggingClassifier
from sklearn.naive_bayes import BernoulliNB,CategoricalNB,ComplementNB,GaussianNB,MultinomialNB
from sklearn.calibration import CalibratedClassifierCV
from sklearn.multioutput import ClassifierChain,MultiOutputClassifier
from sklearn.tree._classes import DecisionTreeClassifier,ExtraTreeClassifier
from sklearn.dummy import DummyClassifier
from sklearn.ensemble._forest import ExtraTreesClassifier,RandomForestClassifier
from sklearn.model_selection._classification_threshold import FixedThresholdClassifier,TunedThresholdClassifierCV
from sklearn.gaussian_process._gpc import GaussianProcessClassifier
from sklearn.ensemble._gb import GradientBoostingClassifier
from sklearn.ensemble._hist_gradient_boosting.gradient_boosting import HistGradientBoostingClassifier
from sklearn.neighbors._classification import KNeighborsClassifier,RadiusNeighborsClassifier
from sklearn.semi_supervised._label_propagation import LabelPropagation,LabelSpreading
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis,QuadraticDiscriminantAnalysis
from sklearn.svm._classes import LinearSVC,NuSVC,SVC
from sklearn.linear_model._logistic import LogisticRegression,LogisticRegressionCV
from sklearn.neural_network._multilayer_perceptron import MLPClassifier
from sklearn.neighbors._nearest_centroid import NearestCentroid
from sklearn.multiclass import OneVsOneClassifier,OneVsRestClassifier,OutputCodeClassifier
from sklearn.linear_model._passive_aggressive import PassiveAggressiveClassifier
from sklearn.linear_model._perceptron import Perceptron
from sklearn.linear_model._ridge import RidgeClassifier,RidgeClassifierCV
from sklearn.linear_model._stochastic_gradient import SGDClassifier
from sklearn.ensemble._stacking import StackingClassifier
from sklearn.ensemble._voting import VotingClassifier
from sklearn.model_selection import train_test_split



regression_models = {
"LinearRegression":LinearRegression,
"Ridge":Ridge,
"Lasso":Lasso,
"ElasticNet":ElasticNet,
"Lars":Lars,
"LassoLars":LassoLars,
"OrthogonalMatchingPursuit":OrthogonalMatchingPursuit,
"BayesianRidge":BayesianRidge,
"ARDRegression":ARDRegression,
"HuberRegressor":HuberRegressor,
"PassiveAggressiveRegressor":PassiveAggressiveRegressor,
"RANSACRegressor":RANSACRegressor,
"TheilSenRegressor":TheilSenRegressor,
"QuantileRegressor":QuantileRegressor
}


classification_models = {"AdaBoostClassifier":AdaBoostClassifier,
"BaggingClassifier":BaggingClassifier,
"BernoulliNB":BernoulliNB,
"CalibratedClassifierCV":CalibratedClassifierCV,
"CategoricalNB":CategoricalNB,
"ClassifierChain":ClassifierChain,
"ComplementNB":ComplementNB,
"DecisionTreeClassifier":DecisionTreeClassifier,
"DummyClassifier":DummyClassifier,
"ExtraTreeClassifier":ExtraTreeClassifier,
"ExtraTreesClassifier":ExtraTreesClassifier,
"FixedThresholdClassifier":FixedThresholdClassifier,
"GaussianNB":GaussianNB,
"GaussianProcessClassifier":GaussianProcessClassifier,
"GradientBoostingClassifier":GradientBoostingClassifier,
"HistGradientBoostingClassifier":HistGradientBoostingClassifier,
"KNeighborsClassifier":KNeighborsClassifier,
"LabelPropagation":LabelPropagation,
"LabelSpreading":LabelSpreading,
"LinearDiscriminantAnalysis":LinearDiscriminantAnalysis,
"LinearSVC":LinearSVC,
"LogisticRegression":LogisticRegression,
"LogisticRegressionCV":LogisticRegressionCV,
"MLPClassifier":MLPClassifier,
"MultiOutputClassifier":MultiOutputClassifier,
"MultinomialNB":MultinomialNB,
"NearestCentroid":NearestCentroid,
"NuSVC":NuSVC,
"OneVsOneClassifier":OneVsOneClassifier,
"OneVsRestClassifier":OneVsRestClassifier,
"OutputCodeClassifier":OutputCodeClassifier,
"PassiveAggressiveClassifier":PassiveAggressiveClassifier,
"Perceptron":Perceptron,
"QuadraticDiscriminantAnalysis":QuadraticDiscriminantAnalysis,
"RadiusNeighborsClassifier":RadiusNeighborsClassifier,
"RandomForestClassifier":RandomForestClassifier,
"RidgeClassifier":RidgeClassifier,
"RidgeClassifierCV":RidgeClassifierCV,
"SGDClassifier":SGDClassifier,
"SVC":SVC,
"StackingClassifier":StackingClassifier,
"TunedThresholdClassifierCV":TunedThresholdClassifierCV,
"VotingClassifier":VotingClassifier,
}




def app(df,indep_cols,dep_var,dependent_type,test_size=.2):
    st.header('Page 3 - Model Building Suite', divider="blue")
    # st.write(df.columns)
    x = df[indep_cols].values
    y = df[dep_var].values
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    if dependent_type == 'Numerical':
        fitted_model = mu.app(xtr,ytr,regression_models)
        return fitted_model
    elif dependent_type == 'Categorical':
        fitted_model = mu.app(xtr,ytr,classification_models)
        return fitted_model
    else:
        return None