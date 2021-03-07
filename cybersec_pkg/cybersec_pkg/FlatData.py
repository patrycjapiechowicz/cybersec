import json
import pandas as pd
import csv


def read_data(path, limiter):
    """
    Args:
        path: path to dataset in jsonl file format
        limiter: number of rows

    Returns:
        data: json dict, where every line is one sample as json
    """
    with open(path) as file:
        data = [json.loads(next(file)) for x in range(limiter)]
    return data


def transform_dll_imports(json_sample):
    """
    Args:
        json_sample: one sample of dataset

    Returns:
        functions_dict: dict with all dll functions name with value True
    """
    imports = sample["imports"]
    functions_dict = {}
    for key in imports.keys():
        functions = imports[key]
        functions_with_values = {key.lower() + "-" + f_name: True for f_name in functions}
        functions_dict.update(functions_with_values)
    return functions_dict


def transform_dict(json_dict):
    """
    Args:
        json_dict: json dict with nested key-value, where value is list

    Returns:
        functions_dict: dict with value as a key and default value True
    """
    result_dict = {}
    for key in json_dict.keys():
        keys = json_dict[key]
        values_with_default = {key.lower() + "-" + f_name: True for f_name in keys}
        result_dict.update(values_with_default)
    return result_dict


def transform_list(json_list):
    """
    Args:
        json_list: json list of values

    Returns:
        functions_dict: dict with all dll functions name with value True
    """
    result_dict = {}
    result_dict.update({i: True for i in json_list})
    return result_dict


def flatten_json(y, separator=''):
    """
    Args:
        y: json object
        separator: separator

    Returns:
        functions_dict: dict with flatten values
    """
    out = {}

    def flatten(x, name=separator):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Extract "sha256", "md5", "appeared", "label" and "avclass" columns to a flat form

def get_simple_column(sample, columns=["sha256", "md5", "appeared", "label", "avclass"]):
    """
    input:
        data: variable with dataset
        columns: list of names extracted columns
    output:
        final_list: list of dicts, one list's element is a one sample of dataset
    """
    simple_dict = {}
    simple_dict.update({column: sample[column] for column in columns})
    return simple_dict


# Extraction columns with list: "histogram", "byteentropy", "exports"

def get_simple_list_from_column(sample, columns=["histogram", "byteentropy", "exports"]):
    """
    input:
        data: variable with dataset
        columns: name of extracted columns (str)
    output:
        final_list: list of dicts, one list's element is a one sample of dataset
    """

    dict_exports = {}
    dict_others = {}
    dict_final = {}

    for column in columns:
        if column == "exports":
            dict_exports.update({column + "_" + str(v).lower(): True for v in sample[column]})
        else:
            dict_others.update({column + "_" + str(i): n for i, n in enumerate(sample[column])})

    dict_final.update(dict_others)
    dict_final.update(dict_exports)

    return dict_final


# Extraction IMPORTS, GENERAL and STRINGS columns

def get_features_from_dict_column(sample, columns="imports"):
    """
    input:
            data
            columns
    output:
            functions_with_valuex
    """
    dict_final = {}
    temp1 = {}
    temp2 = {}
    temp3 = {}

    feature = sample[columns]
    for key in feature.keys():
        content = feature[key]
        if isinstance(content, list) and len(content) != 0:
            if not isinstance(content[0], str):
                temp1.update({columns + "_" + key.lower() + "-" + str(i): cont for i, cont in enumerate(content)})
            else:
                temp2.update({columns + "_" + key.lower() + "-" + str(cont).lower(): True for cont in content})
        else:
            temp3.update({columns + "_" + key: content})

    dict_final.update(temp1)
    dict_final.update(temp2)
    dict_final.update(temp3)
    return dict_final


# Extraction HEADER column

def get_features_from_header(sample):
    """
    input:
        data: data
    output:
        list_final: list of dicts
    """
    headers = sample["header"]
    dict_lists = {}
    dict_others = {}
    dict_final = {}

    for h in headers.keys():
        temp = headers[h]
        for k in temp.keys():

            if isinstance(temp[k], list):
                dict_lists.update({"header_"+h.lower()+"_"+k.lower()+"_"+str(t).lower():True for t in temp[k]})
            else:
                dict_others.update({"header_"+h.lower()+"_"+k.lower():temp[k]})

    dict_final.update(dict_lists)
    dict_final.update(dict_others)
    return dict_final


# Extraction Section column

# Extraction Section column

def get_features_from_section(sample):
    """
    input:
        data: data
    output:
        list_final: list of dicts
    """

    section_entry = sample['section']['entry']  # .text
    section_sections = sample['section']['sections']
    dict_lists_sections = {}
    dict_others_sections = {}
    dict_final = {}
    simple_dict = {}
    simple_dict.update({'section_entry': section_entry})

    for part in section_sections:
        name = part['name']
        for position in ['size', 'entropy', 'vsize', 'props']:
            if position == 'props':
                dict_lists_sections.update(
                    {"section_sections_" + name.lower() + "_" + position + "_" + str(element).lower(): True for element
                     in part[position]})
            else:
                dict_others_sections.update({"section_sections_" + name.lower() + "_" + position: part[position]})
    dict_final.update(dict_lists_sections)
    dict_final.update(dict_others_sections)
    dict_final.update(simple_dict)
    return dict_final


# Extraction DATADIRECTORIES column

def get_features_from_datadirectories(sample):
    """
    input:
        data: data
    output:
        sum_others_datadir: list of dicts
    """

    dict_others_datadir = {}
    datadir = sample["datadirectories"]

    for element in datadir:
        element_name = element['name']
        for position in ['size', 'virtual_address']:
            dict_others_datadir.update({"datadirectories_" + element_name + "_" + position: element[position]})
    return dict_others_datadir

# Extraction IMPORTS column

def get_features_from_imports(sample):
    """
    input:
        data: data
    output:
        sum_others_datadir: list of functions from every dll
    """
    functions_list = []
    imports = sample["imports"]

    for key in imports.keys():
        functions = imports[key]
        values = ['imports.' + key.lower() + "-" + f_name for f_name in functions]
        functions_list.append(values)
    functions_list = [item for sublist in functions_list for item in sublist]
    return {'imports': functions_list}

def write_csv(csv_file_path, sample_list):
    """
    Args:
        csv_file_path: destination path of csv file
        sample_list: list of dicts
    """
    all_keys = set().union(*(d.keys() for d in flatten_dataset))

    try:
        with open(csv_file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_keys)
            writer.writeheader()
            for data in flatten_dataset:
                writer.writerow(data)
    except IOError:
        print("I/O error")

