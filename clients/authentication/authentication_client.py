from httpx import Response
from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema,LoginResponseSchema
from clients.public_http_builder import get_public_httpx_client


class AuthenticationClient(APIClient):
    def login_api(self, request:LoginRequestSchema)-> Response:
        # return self.post("/api/v1/authentication/login",json= request)
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request:RefreshRequestSchema)-> Response:
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self,request:LoginRequestSchema)-> LoginResponseSchema:
         response = self.login_api(request)
         return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client = get_public_httpx_client())