
from clients.courses.courses_client import get_courses_client
from clients.courses.couses_schema import CreateCourseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import  CreateFileRequestShema
from clients.private_http_builder import  AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(

     email =  get_random_email(),
     password =  "string",
     last_name="string",
     first_name="string",
     middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
     email =  create_user_request.email,
     password =  create_user_request.password
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

create_file_request = CreateFileRequestShema(
    filename="image.png",
    directory="string",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print("create file data", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title = "python",
     maxScore = 100,
     minScore = 1,
     description = "Python API course",
     estimatedTime =  "2 weeks",
     previewFileId = create_file_response.file.id,
     createdByUserId = create_user_response.user.id
)

create_file_response = courses_client.create_course(create_course_request)
print("create course data: ", create_file_response)