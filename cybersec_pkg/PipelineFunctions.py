from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin


class CustomTransformer(BaseEstimator, TransformerMixin):
    '''Custom transformer class - does something'''

    def __init__(self, labels):
        self.labels = labels
        self.fited = False

    def fit(self, X, y=None):
        '''Takes and input of data (X) and fits transformer to it, returns transformer object'''
        self.min_val_ = X[self.labels].min()
        self.fited = True
        return self

    def transform(self, X):
        '''Transforms data passed as it should. Returns transformed data.'''
        # make sure that it was fitted
        if(self.fited):
            X = X.copy()  # This is so we do not make changes to the original dataframe
            X[self.labels] = X[self.labels] - self.min_val_
            return X