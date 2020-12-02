import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
import pickle as pk


file = open('Data/train.pkl', 'rb')
df = pk.load(file)
file.close()

X = df.drop(['TenYearCHD'],axis=1)
y = df["TenYearCHD"]


preprocessor = Pipeline([
    ('std_scaler', StandardScaler()),
    ('imputer', SimpleImputer(strategy= 'most_frequent'))
])

final_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', LogisticRegression())])

# final_pipeline = final_pipeline.fit(X, y)
# score = cross_val_score(final_pipeline,X,y)
# print(score)

# Export the model to a file
joblib.dump(final_pipeline, 'model.joblib')