from data_gen_errors import errors_for_utils_data


def get_data(len_data):
    """
    Validation of data len
    :param len_data:
    :return: error or len_data
    """

    if len_data is None:
        return errors_for_utils_data.LenNotProvidedError("len data is not provided!!!")
    if len_data < 0:
        return errors_for_utils_data.LenGetError("len cannot be negative!!!")
    if len_data == 0:
        return errors_for_utils_data.LenGetError("len cannot be 0!!!")
    if len_data >= 1:
        return
    if len_data >= 999:
        return errors_for_utils_data.LenGetError("len cannot be greater than 999!!!")
