# import httpx
# from tools.fakers import fake
# user_create_payload = {
#     "email": fake.email(),
#     "password": "1111",
#     "lastName": "old",
#     "firstName": "valera",
#     "middleName": "string"
# }
#
# response = httpx.post("http://192.168.0.10:8000/api/v1/users", json=user_create_payload)
#
# print(response.json())
# print(response.status_code)