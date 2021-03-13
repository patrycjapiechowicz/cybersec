"""preprocessing pipline"""
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin


# perform a input operation defined for a specified labels
nan_handler = ColumnTransformer(
    [
        ("process_name", "transformer",
            ["labels"]),
        ("process_name_2", "transformer_2",
         ["other labels"]),
    ],
    remainder="passthrough",
)

# thresholds a specified labels with specified rules defined for each label-set
thresholder = ColumnTransformer(
    [
        ("process_name", "transformer",
            ["labels"]),
    ],
    remainder="passthrough",
)


class CustomTransformer(BaseEstimator, TransformerMixin):
    """Custom transformer class - does something"""

    def __init__(self, labels):
        self.labels = labels
        self.fited = False

    def fit(self, X, y=None):
        """Takes and input of data (X) and fits transformer to it, returns transformer object"""
        self.min_val_ = X[self.labels].min()
        self.fited = True
        return self

    def transform(self, X):
        """Transforms data passed as it should. Returns transformed data."""
        # make sure that it was fitted
        if self.fited:
            X = X.copy()  # This is so we do not make changes to the original dataframe
            X[self.labels] = X[self.labels] - self.min_val_
            return X


flat_labels = ['appeared', 'size', 'vsize', 'has_debug', 'exports_general',
               'imports_general', 'has_relocations', 'has_resources',
               'has_signature', 'has_tls', 'sumbols', 'numstrings', 'avlength',
               'printables', 'entropy', 'paths', 'urls', 'registry', 'MZ']
labels_to_standarize = []
labels_to_thresholdize = []
labels_to_encode = []

steps = [('inputize', nan_handler), ('standarize', '_____'),
         ('thresholdize', '_____'), ('encode', '_____'),
         ('PCA', '_____'), ('modeling', '_____')]
pipeline = Pipeline(steps)
