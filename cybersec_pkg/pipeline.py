"""pipeline"""
import pandas as pd
from .flat_data import get_simple_column, get_simple_list_from_column, \
    get_features_from_dict_column, get_features_from_imports, get_features_from_header, \
    get_features_from_section, get_features_from_datadirectories
from .flat_general_strings import transform_strings, transform_general
from .transform_data import transform_section, transform_data_directories, \
    transform_byte_entropy, transform_histogram, \
    transform_imports


def run_transformer(data):
    """
    Function transforms flatten df to df with reduced dimensions based on initial cleaning functions
    Args:
        data: list of dictionaries
    Returns: df - cleaned initially
    """

    flatten_dataset = []
    for sample in data:
        transformed = {}

        transformed.update(get_simple_column(sample))
        transformed.update(get_simple_list_from_column(sample))
        transformed.update(get_features_from_dict_column(sample, columns="strings"))
        transformed.update(get_features_from_dict_column(sample, columns="general"))
        transformed.update(get_features_from_imports(sample))
        transformed.update(get_features_from_header(sample))
        transformed.update(get_features_from_section(sample))
        transformed.update(get_features_from_datadirectories(sample))

        # here we fill with transform data
        flatten_dataset.append(transformed)

    # change all transformed dataset to dataframe object
    df_flat = pd.DataFrame(flatten_dataset)

    # Transform section dimension reduced from 202 to 6
    df_section = transform_section(df_flat)

    # nothing reduced, this will be reduced in 2nd phase

    df_header = df_flat[df_flat.columns[df_flat.columns.str.startswith('header_')]].copy()
    df_header.fillna(False, inplace=True)
    col = df_header.columns[
        df_header.columns.str.startswith(('header_coff_characteristics', 'header_optional_dll'))]
    df_header.loc[:, col] = df_header.loc[:, col].astype('int64')

    # transform strings
    df_strings = transform_strings(df_flat)

    # transform general
    df_general = transform_general(df_flat)

    # transform data directories
    df_data_directories = transform_data_directories(df_flat)

    # transform byte entropy
    df_byte_entropy = transform_byte_entropy(df_flat)

    # transform histogram
    df_histogram = transform_histogram(df_flat)

    # transform imports
    df_imports = transform_imports(df_flat)

    # transform label
    df_label = df_flat["label"].copy()

    # final dataframe

    final = pd.concat(
        [
            df_label,
            df_flat["sha256"],
            df_section,
            df_header,
            df_strings,
            df_general,
            df_data_directories,
            df_byte_entropy,
            df_histogram,
            df_imports,
        ],
        axis=1,
    )

    final.columns = [x.replace("-", "_") for x in final.columns]

    return final
