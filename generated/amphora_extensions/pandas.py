import pandas as pd
import numpy as np
import amphora_client as a10a

def to_df(query_result_page: a10a.QueryResultPage):
    '''
    Converts a QueryResultPage dataset to a Pandas DataFrame, using NumPy np.array
    params:
        query_result_page          amphora_client.QueryResultPage
    returns
        pd.DataFrame
    '''

    data = []
    column_names = []
    for _ in range(len(query_result_page.properties)):
        data.append(np.array(query_result_page.properties[_].values).reshape((len(query_result_page.properties[_].values))))
        column_names.append(query_result_page.properties[_].name)

    # dataframe
    df = pd.DataFrame(data).T
    df.index =  np.array(query_result_page.timestamps)
    df.columns = column_names

    return df
