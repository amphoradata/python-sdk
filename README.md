# python-sdk
A python SDK for Amphora Data

## Open API

The code in `/generated` was produced via the [Open API Generator tool](https://github.com/OpenAPITools/openapi-generator). View the generated docs [here](generated/README.md)

# Samples

## Prerequesits

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