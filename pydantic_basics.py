 # "course": {
 #    "id": "string",
 #    "title": "string",
 #    "maxScore": 0,
 #    "minScore": 0,
 #    "description": "string",
 #    "previewFile": {
 #      "id": "string",
 #      "filename": "string",
 #      "directory": "string",
 #      "url": "https://example.com/"
 #    },
 #    "estimatedTime": "string",
 #    "createdByUser": {
 #      "id": "string",
 #      "email": "users@example.com",
 #      "lastName": "string",
 #      "firstName": "string",
 #      "middleName": "string"
 #    }
 #  }

from pydantic import BaseModel, Field, ConfigDict,HttpUrl, EmailStr,ValidationError
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id:str
    title:str
    max_score:int = Field(alias="maxScore")
    min_score : int = Field(alias="minScore")
    description:str
    preview_File: FileSchema = Field(alias="previewFile")
    estimated_Time:str  = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id = "course-id",
    title="Playwright",
    maxScore = 100,
    minScore = 10,
    description="Playwright",

    previewFile =  FileSchema(
        id = "file-idy",
        url= "http://localhost:8000",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="1 week",
    createdByUser= UserSchema(
        id = "users-id",
        email="users@gmail.com",
        lastName="bogatyrev",
        firstName="denis",
        middleName = "badr"
    )
)

print(course_default_model)

course_dict = {
     "id": "course-id",
     "title": "Playwright",
     "maxScore" : 100,
     "minScore": 100,
     "description": "Playwright",
     "previewFile" : {
        "id" : "file-idy",
         "url": "http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
     "estimatedTime": "string",
     "createdByUser" : {
        "id":"users-id",
        "email": "users@gmail.com",
        "lastName":"bogatyrev",
        "firstName":"denis",
        "middleName" : "badr"
     }

}

course_dict_model = CourseSchema(**course_dict)
print(course_dict_model)

course_json = """{
     "id": "course-id",
     "title": "Playwright",
     "maxScore" : 100,
     "minScore": 100,
     "description": "Playwright",
     "previewFile" : {
        "id" : "file-idy",
         "url": "http://localhost:8000",
        "filename":"file.png",
        "directory":"courses"
    },
     "estimatedTime": "string",
     "createdByUser" : {
        "id":"users-id",
        "email": "users@gmail.com",
        "lastName":"bogatyrev",
        "firstName":"denis",
        "middleName" : "badr"
     }

}"""

try:
    file = FileSchema(
        id="file-idy",
        url= "//localhost:8000",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)

# course_json_model = CourseSchema.model_validate_json(course_json)
# print(course_json_model)
# print(course_json_model.model_dump(by_alias=True))
# print(course_json_model.model_dump_json(by_alias=True))