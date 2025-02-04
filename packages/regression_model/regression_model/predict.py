import numpy as np
import pandas as pd

import math
from regression_model.processing.data_management import load_pipeline
from regression_model.processing.validate_inputs import validate_inputs

from regression_model.config import config
from regression_model import __version__ as _version
from regression_model.config.logging_config import get_logger

_logger = get_logger(logger_name=__name__)


pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}_{_version}.pkl'
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    data = pd.read_json(input_data)
    validated_data = validate_inputs(input_data = data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)
    response = {'predictions': output,'version': _version}

    _logger.info(
        f'Making predictions with model version: {_version}'
        f'Inputs: {validated_data}'
        f'Predictions: {response}'
    )
    return response

