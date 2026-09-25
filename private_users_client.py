from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class UserUpdateRequestDict(TypedDict):

    email: str | None
    password: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.client.get("/api/v1/users/me")

    def get_user_api(self,user_id: str) -> Response:
        return self.client.get(f"/api/v1/users/{user_id}")

    def update_user_api(self,user_id:str,request: UserUpdateRequestDict) -> Response:
        return self.client.patch(f"/api/v1/users/{user_id}", json = request)

    def delete_user_api(self, user_id:str)-> Response:
        return self.client.delete(f"/api/v1/users/{user_id}")