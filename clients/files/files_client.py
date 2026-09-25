from h11 import Response

from clients.api_client import APIClient
from typing import  TypedDict

class CreateFileRequestDict(TypedDict):
    filename: str
    directory:str
    upload_file:str


class FilesClient(APIClient):
    def get_file_api(self,file_id:str) -> Response:
        return self.client.get(f"/api/v1/files/{file_id}")

    def create_file_api(self,request:CreateFileRequestDict)-> Response:
        return self.client.post(f"/api/v1/files",data=request, files= {"upload_file" : open(request["upload_file"], "rb") })

    def delete_file(self, file_id:str) -> Response:
        return self.client.delete(f"/api/v1/files/{file_id}")