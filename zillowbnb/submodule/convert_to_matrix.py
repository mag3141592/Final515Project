"""Converts cleaned listings dataframe into matrix. It also provides metadata for said dataframe"""
import numpy as np
import pandas as pd

def metadata(data_frame, feature_list):
    """
    Creates metadata.
    :params dataframe data_frame:
    :returns dict:
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise ValueError("input must be a pandas Dataframe")

    neighborhood = data_frame.neighbourhood_cleansed.unique()
    neighborhood.sort()
    neighborhood_group = data_frame.neighbourhood_group_cleansed.unique()
    neighborhood_group.sort()
    property_type = data_frame.property_type.unique()
    property_type.sort()
    room_type = data_frame.room_type.unique()
    room_type.sort()

    dict_n = {neighborhood[i]:i for i in range(len(neighborhood))}
    dict_ng = {neighborhood_group[i]:i for i in range(len(neighborhood_group))}
    dict_pt = {property_type[i]:i for i in range(len(property_type))}
    dict_rt = {room_type[i]:i for i in range(len(room_type))}
    columns = feature_list

    return {'neighborhood' : dict_n, 'neighborhood group' : dict_ng, "property type" : dict_pt,
            "room type" : dict_rt, "columns" : columns}

def to_matrix(data_frame, feature_list):
    """
    Converts cleaned dataframe into matrix
    :params dataframe data_frame:
    :return x_var, y_var:
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise ValueError("input must be a pandas Dataframe")

    df2 = data_frame.drop(columns='listing_id')

    df2["neighbourhood_cleansed"].replace(metadata(data_frame,
                                                   feature_list)['neighborhood'], inplace=True)
    df2["neighbourhood_group_cleansed"].replace(metadata(data_frame,
                                                         feature_list)['neighborhood group'],
                                                inplace=True)
    df2["property_type"].replace(metadata(data_frame, feature_list)['property type'], inplace=True)
    df2["room_type"].replace(metadata(data_frame, feature_list)['room type'], inplace=True)

    data = df2.values

    y_var = data[:, -1]

    x_var = np.delete(data, -1, axis=1)

    return x_var, y_var
