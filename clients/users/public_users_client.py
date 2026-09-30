from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from clients.public_http_builder import get_public_httpx_client

# class User(TypedDict):
#
#     id:str
#     email:str
#     lastName: str
#     firstName: str
#     middleName: str
#
# class CreateUserRequestDict(TypedDict):
#     email: str
#     password: str
#     lastName: str
#     firstName: str
#     middleName: str
#
# class CreateUserResponseDict(TypedDict):
#
#     user: User



class PublicUserClient(APIClient):

    def create_user_api(self,request: CreateUserRequestSchema) -> Response:
        return self.client.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self,request:CreateUserRequestSchema)-> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUserClient:
    return PublicUserClient(client = get_public_httpx_client())