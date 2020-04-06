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
    def __init__(self, username: str, password: str, host = "https://app.amphoradata.com"):
        configuration = api.Configuration(host=host)
        authApi = api.AuthenticationApi(api.ApiClient(configuration))
        details = api.LoginRequest(username= username, password= password)
        self.token = authApi.authentication_request_token(login_request= details)
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
                terms_and_conditions_id: str    id reference of the terms and conditions to apply
                labels: [str]                   a list (max 5) of labels
        returns:
            amphora.Amphora
        """
        price= kwargs["price"] if "price" in kwargs else 0
        lat:float= kwargs["lat"] if "lat" in kwargs else None
        lon:float= kwargs["lon"] if "lon" in kwargs else None
        terms_and_conditions_id: str = kwargs["terms_and_conditions_id"] if "terms_and_conditions_id" in kwargs else None
        labels: [str] = kwargs["labels"] if "labels" in kwargs else []
        model = api.CreateAmphora(name = name, 
                                    description=description, 
                                    price= price, 
                                    terms_and_conditions_id= terms_and_conditions_id, 
                                    labels= ",".join(labels),
                                    lat = lat,
                                    lon = lon)
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
