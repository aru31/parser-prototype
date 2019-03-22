import json
import yaml

import text_parser


def convert_yaml(filename):
    """
    function to genrate yaml files
    data: raw structure of dictionary
    """
    data = {
        "filename": filename,
        "parameters": []
    }
    tuple_data = text_parser.pygccxml_text_parser(filename)
    for tuples in tuple_data:
        data_dict = {
            "name": tuples[0],
            "retrun_type": tuples[1],
            "is_virtual": tuples[2],
            "is_static": tuples[3],
            "arguments": tuples[4]
        }
        data['parameters'].append(data_dict.copy())

    with open('sample.yml', 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
