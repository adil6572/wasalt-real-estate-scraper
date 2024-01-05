import pandas as pd
import json
from pprint import pprint
from utils import column_mapping, selected_columns


def flatten_dictionary(input_dict, parent_key='', sep='_'):
    flattened_dict = {}
    for k, v in input_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flattened_dict.update(flatten_dictionary(v, new_key, sep=sep))
        else:
            flattened_dict[k] = v
    return flattened_dict


def clean_data(raw_proprties_dict: list):

    properties_list = []

    for item in raw_proprties_dict:
        flattened_result = flatten_dictionary(item)
        flattened_result.update({item["key"]: item["value"]
                                for item in flattened_result.pop("attributes", [])})
        image_list = []
        properties_list.append(flattened_result)

    df = pd.DataFrame(properties_list)
    df.rename(columns=column_mapping, inplace=True)
    filtered_columns = [col for col in selected_columns if col in df.columns]
    result_df = df[filtered_columns]
    return result_df


if __name__ == "__main__":
    with open('data.json', 'r', encoding='utf-8') as json_file:
        original_proprties = json.load(json_file)

    # Displaying the read data
