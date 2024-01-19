#assignment 1 
#lemm

from sklearn.datasets import load_diabetes
import pandas as pd

diabetes_dataset = load_diabetes()

diabetes_df = pd.DataFrame(diabetes_dataset.data, columns=diabetes_dataset.feature_names)

diabetes_df.columns()

