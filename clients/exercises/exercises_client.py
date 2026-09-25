from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExercisesQueryDict(TypedDict):
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    def get_exercises_api(self, query:GetExercisesQueryDict)-> Response:
        return self.client.get("/api/v1/exercises", params = query)

    def get_exercise_api(self,exercise_id:str)-> Response:
        return self.client.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request:CreateExercisesRequestDict)-> Response:
        return self.client.post("/api/v1/exercises", json = request)

    def update_exercises_api(self,exercise_id: str, request: UpdateExerciseRequestDict)-> Response:
        return self.client.patch(f"/api/v1/exercises{exercise_id}", json = request)

    def delete_exercise_api(self,exercises_id:str)-> Response:
        return self.client.delete(f"/api/v1/exercises/{exercises_id}")
