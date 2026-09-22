from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

class CreateUserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUserClient(APIClient):

    def create_user_api(self,request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)



