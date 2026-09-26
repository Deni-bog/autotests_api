from clients.authentication import authentication_client
from clients.private_http_builder import AuthenticationUserDict
from clients.user.private_users_client import get_private_users_client
from clients.user.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_dict = CreateUserRequestDict(

     email =  get_random_email(),
     password =  "string",
     lastName =   "string",
     firstName =  "string",
     middleName = "string"
)

create_user_response = public_users_client.create_user(create_user_dict)

print("create user data: ", create_user_response)

authentication_user = AuthenticationUserDict(
    email = create_user_dict["email"],
    password= create_user_dict["password"]
)

private_user_client = get_private_users_client(authentication_user)

get_user_response = private_user_client.get_user(create_user_response["user"]["id"])
print("get user data", get_user_response)




