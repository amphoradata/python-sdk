import ntpath

class FileUploader():
    # amphoraApi == amphora_client.AmphoraApi
    def __init__(self, amphoraApi):
        self.amphoraApi = amphoraApi
        self.client = amphoraApi.api_client

    def create_and_upload_file(self, id, path_to_file):
        file_name = self.path_leaf(path_to_file)
        print(f"Using filename: {file_name}")

        upload_response = self.amphoraApi.amphorae_create_file(id, file_name)
        print('created a file')
        self.upload_file(upload_response, path_to_file)
    
    def upload_file(self, upload_response, path_to_file):
        f = open(path_to_file, "rb")
        body=f.read()
        hdrs = self._get_headers(path_to_file)
        response = self.client.rest_client.PUT(upload_response.url, hdrs, body=body)
        if(response.status == 201):
            print("Successfully uploaded")
        else:
            print("Error uploading")
            raise Exception(response.data)

    def _get_headers(self, path_to_file):
        hdrs = dict({
            'x-ms-blob-type' : 'BlockBlob',
            'Content-Type': 'application/octet-stream'
            })
        return hdrs

    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
