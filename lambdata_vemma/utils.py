

import numpy as np
import pandas as pd


rand_50 = np.random.random(50)
rand_100 = np.random.random(100)

class BigData:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def data_head(self):
        return self.dataframe.head()

    def nulls(df):
        return df.isna().sum()

    def test_train_val(df, target_val, feature_vals=df.columns.drop(target)):
        """returns basic train, test, val splits with test and val equal sizes"""

        target = target
        features = feature_vals

        X = df[features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_states=42

        )

        X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.25, random_state=42

        )

        return X_train.shape, y_train.shape, X_val.shape, y_val.shape, X_test.shape, y_test.shape
