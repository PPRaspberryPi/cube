import numpy as np


def construct_2D_audio_frame(cube_size, val):
    """
    :param cube_size:
    :param val: array of size cube_size, contains values from 0 to 100
    :return: frame
    """

    div = 100 / cube_size

    if len(val) != cube_size:
        return None
    translated_values = []
    for x in val:
        translated_values = translated_values + [round(x / div)]

    frame = []

    for x in range(cube_size ** 2):
        frame = frame + [1 if translated_values[x % 8] >= int(np.ceil(((cube_size ** 2) - x) / 8)) else 0]

    return frame

def construct_2D_audio_frame(cube_size, val, layer):
    """
    :param cube_size:
    :param val: array of size cube_size, contains values from 0 to 100
    :return: frame
    """

    div = 100 / cube_size

    if len(val) != cube_size:
        return None
    translated_values = []
    for x in val:
        translated_values = translated_values + [round(x / div)]

    frame = []

    for x in range(cube_size ** 2):
        frame = frame + [1 if np.sqrt(translated_values[x % 8] * translated_values[layer]) >= int(np.ceil(((cube_size ** 2) - x) / 8)) - 1 else 0]

    return frame
