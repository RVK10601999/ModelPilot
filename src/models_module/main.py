import streamlit as st
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet,Lars,LassoLars,OrthogonalMatchingPursuit,BayesianRidge,ARDRegression,HuberRegressor,PassiveAggressiveRegressor,RANSACRegressor,TheilSenRegressor,QuantileRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score

def top_models_with_hyperparameter_tuning(X_train, y_train, X_test, y_test, model_param_grid, top_n, dependent_type):
    models_dc = None
    # Store results
    results = []
    # Perform GridSearchCV for each model
    if dependent_type=='Numerical':
        for model_name, model_info in model_param_grid.items():
            print(f"Running GridSearchCV for {model_name}...")
            try:
                grid_search = GridSearchCV(
                    estimator=model_info['model'],
                    param_grid=model_info['params'],
                    scoring='neg_mean_squared_error',
                    cv=5,
                    n_jobs=-1,
                    verbose=1
                )
                grid_search.fit(X_train, y_train)
                # Evaluate the best model on test data
                best_model = grid_search.best_estimator_
                results.append({
                    "Model->"+model_name+"&"+"Best_Parameters->"+f"{str(grid_search.best_params_)}"+"&"+"Best_score->"+f"{str(grid_search.best_score_)}":best_model,
                    "Best Score": grid_search.best_score_
                })
            except Exception as e:
                print(f"Error with {model_name}: {e}")
        models_dc = sorted(results,key=lambda x:x["Best Score"],reverse=True)[:top_n]
    elif dependent_type=='Categorical':
        for model_name, config in model_param_grid.items():
            print(f"Running GridSearchCV for {model_name}...")
            try:
                grid_search = GridSearchCV(
                    estimator=config["model"],
                    param_grid=config["params"],
                    scoring='accuracy',
                    cv=5,
                    n_jobs=-1
                )
                grid_search.fit(X_train, y_train)
                # Evaluate the best model on test data
                best_model = grid_search.best_estimator_
                y_pred_ts = best_model.predict(X_test)
                y_pred_tr = best_model.predict(X_train)
                test_score = accuracy_score(y_test, y_pred_ts)
                train_score = accuracy_score(y_train, y_pred_tr)
                # Store the result
                results.append({
                    "Model->"+model_name+"&"+"Train_score->"+f"{str(train_score)}"+"&"+"Test_score->"+f"{str(test_score)}": best_model,
                    "Training Score":train_score
                })
            except Exception as e:
                print(f"Error with {model_name}: {e}")
        models_dc = sorted(results,key=lambda x:x['Training Score'],reverse=True)[:top_n]
    return models_dc


def app(df,number_of_models,indep_cols,dep_var,dependent_type,cat_param_grid,num_param_grid,test_size=.2):
    st.header('Page 3 - Model Building Suite', divider="blue")
    # st.write(df.columns)
    st.session_state.top_models = None
    x = df[indep_cols].values
    y = df[dep_var].values
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    if dependent_type == 'Numerical':
        st.session_state.top_models = top_models_with_hyperparameter_tuning(xtr, ytr, xts, yts, num_param_grid, number_of_models,dependent_type)
    elif dependent_type == 'Categorical':
        st.session_state.top_models = top_models_with_hyperparameter_tuning(xtr, ytr, xts, yts, cat_param_grid, number_of_models,dependent_type)
    return st.session_state.top_models
