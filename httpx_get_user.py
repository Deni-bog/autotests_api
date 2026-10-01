# import json
# import token
#
# import httpx
# from tools.fakers import fake
#
# user_create_payload = {
#     "email": fake.email(),
#     "password": "1111",
#     "lastName": "old",
#     "firstName": "valera",
#     "middleName": "string"
# }
#
# create_user_response = httpx.post("http://192.168.0.10:8000/api/v1/users", json=user_create_payload)
# create_user_response_data = create_user_response.json()
#
# print("Create users data: ",create_user_response_data)
# print("Create users Status code: ",create_user_response.status_code)
#
# login_payload = {
#     "email": user_create_payload["email"],
#     "password": user_create_payload["password"]
# }
#
# login_response = httpx.post("http://192.168.0.10:8000/api/v1/authentication/login", json = login_payload)
#
# login_response_data = login_response.json()
# print("login data: ",login_response_data)
#
# get_user_headers = {
#     "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
# }
#
# get_user_response = httpx.get(f"http://192.168.0.10:8000/api/v1/users/{create_user_response_data["users"]["id"]}", headers = get_user_headers)
#
# get_user_response_data = get_user_response.json()
#
# print("get users data: ", get_user_response_data)