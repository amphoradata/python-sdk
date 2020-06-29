from logging import getLogger
logger = getLogger('client.py')

import amphora_api_client as api
from amphora.amphora import Amphora
from amphora.base import Base

# metadata objects
# GET
# CREATE
# UPDATE
# DELETE

# for data objects
# PUSH
# PULL

# management
# SHARE


class Credentials:
    """
    A container for your Amphora Data Credentials
    params:
        username: str           Your Amphora Data username
        password: str           Your password
    """
    def __init__(self,
                 username: str,
                 password: str,
                 host="https://app.amphoradata.com",
                 verify_ssl = True):
        configuration = api.Configuration(host=host)
        print(host)
        configuration.verify_ssl = verify_ssl
        authApi = api.AuthenticationApi(api.ApiClient(configuration))
        details = api.LoginRequest(username=username, password=password)
        self.token = authApi.authentication_request_token(
            login_request=details)
        self.configuration = configuration


class AmphoraDataRepositoryClient(Base):
    """
    The high level client for interacting with an Amphora Data Repository
    params:
        username: str           Your Amphora Data username
        password: str           Your password
    """
    def __init__(self, credentials: Credentials):
        configuration = credentials.configuration
        configuration.api_key["Authorization"] = "Bearer " + credentials.token
        Base.__init__(self, api.ApiClient(configuration=configuration))

    def create_amphora(self, name: str, description: str, **kwargs) -> Amphora:
        """
        Creates a new Amphora
        params:
            name: str                       the name of the Amphora
            description :str                a description of the Amphora
            **kwargs:
                price: float                    a monthly fee (in AUD)
                lat: float                      latitude
                lon: float                      longitude
                terms_of_use_id: str            id reference of the terms of use to apply
                labels: [str]                   a list (max 5) of labels
        returns:
            amphora.Amphora
        """
        price = kwargs["price"] if "price" in kwargs else 0
        lat: float = kwargs["lat"] if "lat" in kwargs else None
        lon: float = kwargs["lon"] if "lon" in kwargs else None
        terms_of_use_id: str = kwargs[
            "terms_of_use_id"] if "terms_of_use_id" in kwargs else None
        labels: [str] = kwargs["labels"] if "labels" in kwargs else []
        model = api.CreateAmphora(
            name=name,
            description=description,
            price=price,
            terms_of_use_id=terms_of_use_id,
            labels=",".join(labels),
            lat=lat,
            lon=lon)
        details = api.AmphoraeApi(self.apiClient).amphorae_create(model)
        return Amphora(self.apiClient, details.id)

    def get_amphora(self, amphora_id: str) -> Amphora:
        """
        Gets an object to interact with the Amphora
        params:
            amphora_id: str         the id of the amphora to get
        returns:
            amphora.Amphora
        """
        return Amphora(self.apiClient, amphora_id)

    def get_self(self) -> api.AmphoraUser:
        """
        Gets the metadata of the logged in user
        returns:
            amphora_api_client.AmphoraUser
        """
        usersApi = api.UsersApi(self.apiClient)
        return usersApi.users_read_self()
    
    def buy_amphora(self, amphora_id):
        
        """
        Buys an amphora with your credentials
        Amphora id needs to be supplied
        """
        
        purchaseAPI = api.AmphoraeApi(self.apiClient)
        sep=" "
        print(sep.join(['Trying to buy Amphora with id', amphora_id]))
        try:
            buyAmphora = purchaseAPI.purchases_purchase(amphora_id)
        except:
            buyAmphora = "Something went wrong, Amphora couldn't be purchased"
        return buyAmphora
    
    def get_your_amphorae(self):
        # self is client

        try:
            queryApi = api.AmphoraeApi(self.apiClient)
            your_amphora_list = queryApi.amphorae_list()
            print('Got the list of your Amphorae')
        except:
            print('Something went wrong, couldnt get the list of your Amphorae')

        return your_amphora_list

    def search_for_amphorae(self, **kwargs):
        """
        Get a list of amphora matching a search
        params:
            lat: float = kwargs["lat"] if "lat" in kwargs else None
            lon: float = kwargs["lon"] if "lon" in kwargs else None
            dist: float = kwargs["distance"] if "distance" in kwargs else None
            term: str = kwargs["term"] if "term" in kwargs else None
            labels: [str] = kwargs["labels"] if "labels" in kwargs else []

        """
        lat: float = kwargs["lat"] if "lat" in kwargs else None
        lon: float = kwargs["lon"] if "lon" in kwargs else None
        dist: float = kwargs["dist"] if "dist" in kwargs else 20
        term: str = kwargs["term"] if "term" in kwargs else None
        labels: [str] = kwargs["labels"] if "labels" in kwargs else []
        search_type: str = kwargs["search_type"] if "search_type" in kwargs else 'AND'
        
        your_amphora_list = []
        
        sep = " "
        
        if search_type == 'AND':         
            try:
                queryApi = api.SearchApi(self.apiClient)
                your_amphora_list.append(queryApi.search_search_amphorae(lat = lat, lon = lon, dist = dist,term = term, labels = labels))
                print('Got the list of your Amphora')
            except:
                print('Something went wrong, couldnt get the list of your Amphorae')
        elif search_type == 'OR':    
            if lat is not None:
                print(sep.join(['Searching for Amphoras near',str(lat),str(lon)]))
                try:
                    queryApi = api.SearchApi(self.apiClient)
                    your_amphora_list.append(queryApi.search_search_amphorae(lat = lat, lon = lon, dist = dist))
                    print(len(your_amphora_list[0]))
                    print('Got the list of your Amphorae')
                except:
                    print('Something went wrong, couldnt get the list of your Amphorae')
        
            if term is not None:
                print(sep.join(['Searching for Amphoras containing',term]))
                try:
                    queryApi = api.SearchApi(self.apiClient)
                    your_amphora_list.append(queryApi.search_search_amphorae(term = term))
                    print(len(your_amphora_list[0]))
                    print('Got the list of your Amphorae')
                except:
                    print('Something went wrong, couldnt get the list of your Amphorae')
                
            if len(labels) > 0:
                print(sep.join(['Searching for Amphoras with labels',labels]))
                try:
                    queryApi = api.SearchApi(self.apiClient)
                    your_amphora_list.append(queryApi.search_search_amphorae(labels = labels))
                    print(len(your_amphora_list[0]))
                    print('Got the list of your Amphorae')
                except:
                    print('Something went wrong, couldnt get the list of your Amphorae')
        else:
            print('Couldnt determine search type')

        return your_amphora_list