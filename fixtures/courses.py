from clients.courses.courses_client import get_courses_client, CoursesClient
from clients.courses.couses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.users import function_user, UserFixture
from fixtures.files import FileFixture
import pytest
from pydantic import BaseModel

class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response:CreateCourseResponseSchema
@pytest.fixture()
def courses_client(function_user:UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture()
def create_course(function_file:FileFixture, courses_client:CoursesClient, function_user:UserFixture):
    request = CreateCourseRequestSchema(previewFileId=function_file.response.file.id, createdByUserId = function_user.response.user.id)
    response =courses_client.create_course(request)
    return CoursesFixture(request= request,response=response)


