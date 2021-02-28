import numpy as np
import pandas as pd


def get_non_standard_section_ratio(row, good_sections=[]):
    """
    Functions returns ratio of non standard sections in sections field. This function is used in apply
    Args:
        row: row of df
        good_sections: list of section names considered as normal/standard
    Return:
        ratio of #non standard sections/ # all sections

    """

    labels = row[~np.isnan(row)].index

    list_of_names = [k.replace('section_sections_', "").replace('_entropy', "") for k in labels]

    proper_filter = [lab for lab in list_of_names if lab not in good_sections]

    if len(list_of_names) == 0:
        return np.NaN
    else:
        return len(proper_filter) / len(list_of_names)


def transform_section(df_flat):
    """
    Function transform column section_entry and section_sections
    Inputs:
        df_flat: flatten data frame
    output:
        df_cleaned: reduced column of sections with new/removed columns
    """
    # filter columns section related
    df_section = df_flat[df_flat.columns[df_flat.columns.str.startswith('section_')]].copy()

    # drop columns with size and vsize
    df_section.drop(df_section.columns[df_section.columns.str.contains('_size')], axis=1, inplace=True)
    df_section.drop(df_section.columns[df_section.columns.str.contains('_vsize')], axis=1, inplace=True)

    # create list of standard sections
    # source: https://keystrokes2016.wordpress.com/2016/06/03/pe-file-structure-sections/
    standard_entries = ['.text', '.bss', '.rdata', '.data', '.rsrc', '.edata', '.idata', '.pdata', '.debug']

    # Section entry
    # 1 - entry is in standard entry, 0 - entry is not standard
    df_section['section_has_non_standard_entry'] = np.where(df_section['section_entry'].isin(standard_entries), 0, 1)

    # Section - sections

    # count number of sections
    df_section['section_cnt'] = df_section[df_section.columns[df_section.columns.str.contains('_entropy')]].apply(
        lambda x: sum(x >= 0), axis=1)

    # count sections which contain high entropy (>6)
    df_section['section_high_entropy_cnt'] = df_section[
        df_section.columns[df_section.columns.str.contains('_entropy')]].apply(lambda x: sum(x >= 6), axis=1)

    # create new column: section_high_entropy ratio
    df_section['section_high_entropy_ratio'] = df_section['section_high_entropy_cnt'] / df_section['section_cnt']

    # create new column: max section entropy
    df_section['section_entropy_max'] = df_section[df_section.columns[df_section.columns.str.contains('_entropy')]].max(
        axis=1)

    # calculate ratio of non standard sections in number of sections
    df_section['section_has_non_standard_sections_ratio'] = df_section[
        df_section.columns[df_section.columns.str.endswith('_entropy')]].apply(
        lambda x: get_non_standard_section_ratio(x, standard_entries), axis=1)

    # drop of non relevant columns
    df_section.drop(df_section.columns[df_section.columns.str.contains('section_sections')], axis=1, inplace=True)
    df_section.drop(df_section.columns[df_section.columns.str.contains('section_entry')], axis=1, inplace=True)

    return df_section
