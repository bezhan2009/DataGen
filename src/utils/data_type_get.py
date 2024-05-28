from src.data_gen_errors import errors_for_utils_data


def type_get(type_element):
    if type_element == 'int':
        return int
    elif type_element == 'float':
        return float
    elif type_element == 'str':
        return str
    elif type_element == 'bool':
        return bool
    elif type_element == 'list':
        return list
    elif type_element == 'dict':
        return dict
    elif type_element == 'tuple':
        return tuple
    elif type_element == 'set':
        return set

    else:
        return errors_for_utils_data.TypeGetError("Unknown data type")

