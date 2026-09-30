# import httpx
#
#
# login_payload = {
#     "email": "users@example.com",
#     "password": "string"
# }
#
# # login_response = httpx.post("http://192.168.0.10:8000/api/v1/authentication/login", json = login_payload)
# login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json = login_payload)
# login_response_data = login_response.json()
# print("login data: ",login_response_data)
#
# client = httpx.Client(
#     # base_url="http://192.168.0.10:8000",
#     base_url="http://127.0.0.1:8000",
#     timeout = 100,
#     headers={"Authorization" : f"Bearer {login_response_data["token"]['accessToken']}"}
#     )
# response = client.get("/api/v1/users/me")
# print(response.json())
#
