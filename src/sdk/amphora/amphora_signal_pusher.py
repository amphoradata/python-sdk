from logging import getLogger
logger = getLogger('amphora_signal_pusher.py')
import pandas as pd

import amphora_api_client as api
from amphora.base import Base
from amphora.errors import SignalNotExistError, InvalidDataError
import amphora.utilities as utils


class AmphoraSignalPusher(Base):
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        Base.__init__(self, apiClient)

    def push(self, df: pd.DataFrame = None):
        dictionaries = df.to_dict(orient='records')
        self.push_signals_dictionaries(dictionaries)

    def push_signals_dictionaries(self, dictionaries: [dict]):
        signals = self.amphoraeApi.amphorae_signals_get_signals(self._id)
        for d in dictionaries:
            validate_dictionary(signals, d)

        self.amphoraeApi.amphorae_signals_upload_signal_batch2(
            self._id, dictionaries)


def validate_dictionary(signals: [api.Signal], dictionary: dict):
    for p in dictionary.keys():
        isInSignals = False
        for s in signals:
            if p == s._property:
                isInSignals = True
            if p == 't':
                isInSignals = True
        if isInSignals == False:
            raise SignalNotExistError(p)

        v = dictionary[p]
        if utils.isNumber(v) or utils.isString(v) or v is None:
            pass
        elif p == 't':
            pass
        else:
            raise InvalidDataError(
                f'the value {v} for key {p} neither string nor number')
