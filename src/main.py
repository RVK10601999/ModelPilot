from data_loader_module import main as dlm_app
from preproc_module import main as ppm_app

#PAGE1
df,dep_var,dependent_type,indep_ls = dlm_app.app()
#PAGE2
processed_df = ppm_app.app(df,dep_var,dependent_type,indep_ls)