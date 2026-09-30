import httpx
from tools.fakers import  get_random_email

user_create_payload = {
    "email": get_random_email(),
    "password": "1111",
    "lastName": "old",
    "firstName": "valera",
    "middleName": "string"
}

create_user_response = httpx.post("http://192.168.0.10:8000/api/v1/users", json=user_create_payload)
create_user_response_data = create_user_response.json()

print("Create users data: ",create_user_response_data)
print("Create users Status code: ",create_user_response.status_code)

login_payload = {
    "email": user_create_payload["email"],
    "password": user_create_payload["password"]
}

login_response = httpx.post("http://192.168.0.10:8000/api/v1/authentication/login", json = login_payload)

login_response_data = login_response.json()
print("login data: ",login_response_data)

create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

create_file_response = httpx.post("http://192.168.0.10:8000/api/v1/files",
data = {"filename": "test_image.png", "directory" : "courses"},
files = {"upload_file" : open("./testdata/files/test_image.png", "rb") },
headers = create_file_headers, timeout= 30)

create_file_response_data = create_file_response.json()

print("create file response",create_file_response_data)