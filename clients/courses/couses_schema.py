from pydantic import BaseModel, Field
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema

class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description : str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    user_id: str = Field(alias="UserID")

class CreateCourseRequestSchema(BaseModel):
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")

class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    title: str | None
    max_score: int | None =  Field(alias="maxScore")
    min_score: int | None =  Field(alias="minScore")
    description: str | None
    estimated_time: int | None = Field(alias="estimatedTime")

