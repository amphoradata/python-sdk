from amphora.client import AmphoraClient, Credentials

credentials = Credentials("rian@amphoradata.com", "Password1!")
client = AmphoraClient(credentials)
amphora_id = "1227a860-0571-4542-942f-dd36cc13f810"
me = client.get_self()
print(me)

amphora = client.get_amphora(amphora_id)
print(amphora.metadata)
files = amphora.get_files()
print(files)
amphora_file = amphora.get_file("Nola.png")
attr = amphora_file.get_attributes()
# amphora_file.download("trst.png") // bug