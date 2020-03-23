# coding: utf-8

# flake8: noqa

"""
    Amphora Data Api

    API for interacting with the Amphora Data platform.  # noqa: E501

    The version of the OpenAPI document: 0.8.4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.8.4"

# import apis into sdk package
from amphora_api_client.api.amphorae_api import AmphoraeApi
from amphora_api_client.api.authentication_api import AuthenticationApi
from amphora_api_client.api.market_api import MarketApi
from amphora_api_client.api.organisations_api import OrganisationsApi
from amphora_api_client.api.search_api import SearchApi
from amphora_api_client.api.time_series_api import TimeSeriesApi
from amphora_api_client.api.users_api import UsersApi
from amphora_api_client.api.version_api import VersionApi

# import ApiClient
from amphora_api_client.api_client import ApiClient
from amphora_api_client.configuration import Configuration
from amphora_api_client.exceptions import OpenApiException
from amphora_api_client.exceptions import ApiTypeError
from amphora_api_client.exceptions import ApiValueError
from amphora_api_client.exceptions import ApiKeyError
from amphora_api_client.exceptions import ApiException
# import models into sdk package
from amphora_api_client.models.account import Account
from amphora_api_client.models.address import Address
from amphora_api_client.models.aggregate_series import AggregateSeries
from amphora_api_client.models.aggregate_variable import AggregateVariable
from amphora_api_client.models.amphora_user import AmphoraUser
from amphora_api_client.models.attribute_store import AttributeStore
from amphora_api_client.models.basic_amphora import BasicAmphora
from amphora_api_client.models.basic_amphora_all_of import BasicAmphoraAllOf
from amphora_api_client.models.category_set import CategorySet
from amphora_api_client.models.classification import Classification
from amphora_api_client.models.create_amphora import CreateAmphora
from amphora_api_client.models.create_amphora_all_of import CreateAmphoraAllOf
from amphora_api_client.models.date_time_range import DateTimeRange
from amphora_api_client.models.detailed_amphora import DetailedAmphora
from amphora_api_client.models.detailed_amphora_all_of import DetailedAmphoraAllOf
from amphora_api_client.models.edit_amphora import EditAmphora
from amphora_api_client.models.edit_amphora_all_of import EditAmphoraAllOf
from amphora_api_client.models.entity import Entity
from amphora_api_client.models.entry_point import EntryPoint
from amphora_api_client.models.event_property import EventProperty
from amphora_api_client.models.fuzzy_search_response import FuzzySearchResponse
from amphora_api_client.models.generic_response import GenericResponse
from amphora_api_client.models.get_events import GetEvents
from amphora_api_client.models.get_series import GetSeries
from amphora_api_client.models.name import Name
from amphora_api_client.models.numeric_variable import NumericVariable
from amphora_api_client.models.organisation import Organisation
from amphora_api_client.models.organisation_all_of import OrganisationAllOf
from amphora_api_client.models.paged_response import PagedResponse
from amphora_api_client.models.poi import Poi
from amphora_api_client.models.position import Position
from amphora_api_client.models.problem_details import ProblemDetails
from amphora_api_client.models.property_values import PropertyValues
from amphora_api_client.models.property_values_all_of import PropertyValuesAllOf
from amphora_api_client.models.query_request import QueryRequest
from amphora_api_client.models.query_result_page import QueryResultPage
from amphora_api_client.models.query_result_page_all_of import QueryResultPageAllOf
from amphora_api_client.models.restriction import Restriction
from amphora_api_client.models.restriction_kind import RestrictionKind
from amphora_api_client.models.result import Result
from amphora_api_client.models.search_parameters import SearchParameters
from amphora_api_client.models.signal import Signal
from amphora_api_client.models.summary import Summary
from amphora_api_client.models.terms_and_conditions import TermsAndConditions
from amphora_api_client.models.token_request import TokenRequest
from amphora_api_client.models.tsx import Tsx
from amphora_api_client.models.update_signal import UpdateSignal
from amphora_api_client.models.upload_response import UploadResponse
from amphora_api_client.models.variable import Variable
from amphora_api_client.models.viewport import Viewport

