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

* You must have an account at beta.amphoradata.com
* You should have git on your machine.
* You should have [Docker installed](https://docs.docker.com/) on your machine.
* You should have a bash shell to run the scripts.

## Running the sample

* Clone this repository `git clone https://github.com/amphoradata/python-sdk`
* Set your username and password [here](run-container.sh)
* Run `build-container.sh`
* Run `run-container.sh`

You will see your profile information printed as JSON on the console.


# Open API

The code in `/generated` was produced via the [Open API Generator tool](https://github.com/OpenAPITools/openapi-generator). View the generated docs [here](generated/README.md)