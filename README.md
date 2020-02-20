# Amphora Data Python SDK

[![Build Status](https://dev.azure.com/amphoradata/Public/_apis/build/status/amphoradata.python-sdk?branchName=master)](https://dev.azure.com/amphoradata/Public/_build/latest?definitionId=7&branchName=master)

> This project is still 0.x and does not have a stable API.

## Install

```sh
pip install amphoradata
```

# Usage

```py
import amphora_client as a10a
from amphora_client.configuration import Configuration
# authenticate
configuration = Configuration()
auth_api = a10a.AuthenticationApi(a10a.ApiClient(configuration)) # creates an unauthenticated client
token = auth_api.authentication_request_token(token_request = a10a.TokenRequest(username='username', password='*****' ))
configuration.api_key["Authorization"] = "Bearer " + token
# read user info
users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration)) # creates an authenticated client
print(users_api.users_read_self())
```

# Samples

Check out the samples in the `samples/` directory.

## Dependencies

* You must have an account at [app.amphoradata.com](https://app.amphoradata.com)

# Open API

The code in `/generated` was produced via the [Open API Generator tool](https://github.com/OpenAPITools/openapi-generator). View the generated docs [here](generated/README.md)