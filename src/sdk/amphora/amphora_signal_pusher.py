import amphora_api_client as api
from amphora.errors import SignalNotExistError, InvalidDataError
import amphora.utilities as utils
import pandas as pd

class AmphoraSignalPusher:
    def __init__(self, apiClient: api.ApiClient, amphora_id: str):
        self._id = amphora_id
        self._apiClient = apiClient
        self._amphoraApi = api.AmphoraeApi(apiClient)


    def push(self, df: pd.DataFrame = None):
        dictionary = df.to_dict(orient = 'records')
        self.push_signals_dict(dictionary)

    def push_signals_dict(self, dictionary: dict):
        signals = self._amphoraApi.amphorae_signals_get_signals(self._id)
        validate_dictionary(signals, dictionary)
        print(dictionary)
        # self._amphoraApi.amphorae_signals_upload_signal_batch2(self._id, dictionary)


def validate_dictionary(signals: [api.Signal], dictionary: dict):
    for p in dictionary.keys:
        isInSignals = False
        for s in signals:
            if s._property == p:
                isInSignals = True
        if isInSignals == False:
            raise SignalNotExistError(p)

    for v in dictionary.values:
        if utils.isNumber(v) or utils.isString(v):
            pass
        else:
            raise InvalidDataError()
