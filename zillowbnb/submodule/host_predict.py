"""Predicts price based on our xgb regressor model"""

from os.path import dirname, abspath, join

import numpy as np
from scipy.special import boxcox1p
from sklearn.externals import joblib
from xgboost import XGBRegressor

# Find data directory relative to current directory
THIS_DIR = dirname(__file__)
DATA_DIR = abspath(join(THIS_DIR, '../..', 'data'))

def predict_input(data, city):
    """
    predicts price using the saved models
    :params data array:
    :params city string:
    :returns price prediction:
    """

    #in case it only predicts one row
    if data.shape == (38,):
        data = data[np.newaxis, :]

    #imports model
    regressor = joblib.load(DATA_DIR + "/" +  city + ".joblib.dat")

    #boxcox transforms features
    boxcox_data = boxcox1p(data, 0.15) + 1
    xgb_pred = np.expm1(regressor.predict(boxcox_data))
    return xgb_pred
