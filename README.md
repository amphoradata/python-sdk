# Amphora Data Python SDK

[![Build Status](https://dev.azure.com/amphoradata/Public/_apis/build/status/amphoradata.python-sdk?branchName=master)](https://dev.azure.com/amphoradata/Public/_build/latest?definitionId=7&branchName=master)

> This project is still 0.x and does not have a stable API.

## Install

```sh
pip install amphoradata
```

# Usage

```py
from amphora.client import AmphoraClient, Credentials

# username and password credentials should not be persisted in code
credentials = Credentials("rian@amphoradata.com", "My Password")
client = AmphoraClient(credentials)

# reference an existing amphora
amphora = client.get_amphora("e6097df0-952c-46a6-84b0-ccc29bf1b0f7")

# upload a file to an Amphora
amphora.push_file("/path/to/a/file")

# share with your collaborators
amphora.share_with("my_friends_email@ghotmail.com")

```

# Samples

Check out the samples in the `samples/` directory.

> You must have an account at [app.amphoradata.com](https://app.amphoradata.com)

# Docs

Check our our official docs page at [docs.amphoradata.com](https://docs.amphoradata.com) or view the Open API Spec docs [here](./src/sdk/README.md)

# Contributing

We welcome pull requests! This project is constantly evolving, and we're always tring to improve.

Feel free to open an issue if you have feature requests, or are experiencing bugs.

We also use [gitter](https://gitter.im/amphoradata/community).

