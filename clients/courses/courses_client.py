from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient

class GetCoursesQueryDict(TypedDict):
    userId: str

class CreateCourseRequestDict(TypedDict):
     title: str
     maxScore: int
     minScore: int
     description: str
     estimatedTime: str
     previewFileId: str
     createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CoursesClient(APIClient):
    def get_courses_api(self,query:GetCoursesQueryDict) -> Response:
        return self.client.get("/api/v1/courses", params = query)

    def get_course_api(self,course_id :str ) -> Response:
        return self.client.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self,request:CreateCourseRequestDict) -> Response:
         return self.client.post("f/api/v1/courses/", json=request)

    def update_course_api(self,request: UpdateCourseRequestDict) -> Response:
        return  self.client.patch("f/api/v1/courses/", json=request)

    def dele_course_api(self,course_id:str)-> Response:
        return self.client.delete(f"/api/v1/courses/{course_id}")