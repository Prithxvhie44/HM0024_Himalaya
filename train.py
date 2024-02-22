import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import numpy as np


data = pd.read_csv('mutual-funds.csv')

print(data.columns)

feature_cols = [
        'min_sip', 'min_lumpsum', 'expense_ratio',
        'fund_size_cr', 'fund_age_yr', 'sortino', 'alpha', 'sd',
        'beta', 'sharpe', 'risk_level', 'rating',
        ]

predictor_cols = [ 'returns_1yr', 'returns_3yr', 'returns_5yr' ]

impute_cols = [ 'sortino', 'alpha', 'sd', 'beta', 'sharpe' ]

data.replace(inplace=True, to_replace='-', value=np.nan)

X = data[feature_cols]

imputer = SimpleImputer()

X[impute_cols] = imputer.fit_transform(X[impute_cols])

y = data[predictor_cols]

imputer = SimpleImputer(strategy='mean')
y = imputer.fit_transform(y)

train_x, test_x, train_y, test_y = train_test_split(X,y)

print(len(train_x))
print(len(train_y))
print(len(test_x))
print(len(test_y))

model = RandomForestRegressor()

model.fit(train_x, train_y)

print(model.score(test_x, test_y))

