
credentials = new Credentials("username", "password")
# or 
credentials = new Credentials(token: "your_jwt_token")

# Reading from the server

client = new AmphoraClient(credentials)
amphora = client.get_amphora("amphora_id")
search_results = client.search_amphora("search term")
files = amphora.get_files()
a_file = amphora.get_file("file_name") # returns something like a "file pointer"

# getting data
data = a_file.pull() # the raw data

signals = amphora.get_signals() # should return some kind of signals wrapper thing
signal = amphora.get_signal("property_name")

signal_data = signals.pull()
pandas_df = signal_data.to_pandas()
pandas_df_single = signal.pull()

# upload data

amphora = client.create_amphora(name= "hi", description = "gday", etc= "the others")
amphora.push_file("path/to/a/file", filename="a different filename", attributes = {})

amphora.share_with("isaac@amphoradata.com")

amphora.create_restriction()
amphora.get_restriction()
amphora.update_restriction()
amphora.delete_restriction()

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

# reserved for future use
# APPLY