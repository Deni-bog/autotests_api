from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.courses.couses_schema import CreateCourseRequestSchema,CreateCourseResponseSchema,UpdateCourseRequestSchema,GetCoursesQuerySchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

class CoursesClient(APIClient):
    def get_courses_api(self,query:GetCoursesQuerySchema) -> Response:
        return self.get("/api/v1/courses", params = query.model_dump())

    def get_course_api(self,course_id :str ) -> Response:
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self,request:CreateCourseRequestSchema) -> Response:
         return self.post("/api/v1/courses", json= request.model_dump(by_alias=True))

    def update_course_api(self,request: UpdateCourseRequestSchema) -> Response:
        return  self.patch("/api/v1/courses", json=request.model_dump(by_alias=True))

    def dele_course_api(self,course_id:str)-> Response:
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema)-> CoursesClient:
    return CoursesClient(client = get_private_http_client(user))