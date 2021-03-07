def transform_general(df_flat):
    """
    Function transform column general and strings
    Inputs:
        df_flat: flatten data frame
    output:
        df_cleaned: reduced dataset
    """
    # filter columns general related
    df_general = df_flat[['general_size','general_vsize','general_has_debug','general_exports','general_imports','general_has_relocations','general_has_resources','general_has_signature','general_has_tls','general_symbols']]
    
     # drop columns with exports,imports,symbols
    df_general.drop('general_exports', axis=1, inplace=True)
    df_general.drop('general_imports', axis=1, inplace=True)
    df_general.drop('general_symbols', axis=1, inplace=True)
    return df_general

def transform_strings(df_flat):
    """
    Function transform column general and strings
    Inputs:
        df_flat: flatten data frame
    output:
        df_cleaned: reduced dataset
    """
    # filter columns strings related
    df_strings = df_flat[df_flat.columns[df_flat.columns.str.startswith('strings_')]].copy()
    # drop columns with exports,imports,symbols
    df_strings.drop('strings_avlength', axis=1, inplace=True)
    df_strings.drop('strings_paths', axis=1, inplace=True)
    df_strings.drop('strings_urls', axis=1, inplace=True)
    df_strings.drop('strings_registry', axis=1, inplace=True)

    return df_strings
