
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExercisesRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
from clients.user.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
     email =  get_random_email(),
     password =  "string",
     lastName =   "string",
     firstName =  "string",
     middleName = "string"
)

create_user_response = public_user_client.create_user(create_user_request)
authentication_user = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

files_client = get_files_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="string",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print("create file response: ", create_file_response)


course_client = get_courses_client(authentication_user)

create_course_request = CreateCourseRequestDict(
     title = "python",
     maxScore = 100,
     minScore = 1,
     description = "Python API course",
     estimatedTime =  "2 weeks",
     previewFileId = create_file_response["file"]["id"],
     createdByUserId = create_user_response["user"]["id"]
)

create_course_response = course_client.create_course(create_course_request)
print("create course response: ", create_course_response)
exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExercisesRequestDict(
    title = "String",
    courseId = create_course_response["course"]["id"],
    maxScore = 100,
    minScore = 10,
    orderIndex =  1,
    description =  "namana",
    estimatedTime = "1 day"

)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise Response: ", create_exercise_response)