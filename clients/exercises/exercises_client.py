from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    courseId: str

class Exercise(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    exercise:Exercise
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

class UpdateExerciseResponseDict(TypedDict):
    exercise:Exercise


class ExercisesClient(APIClient):
    def get_exercises_api(self, query:GetExercisesQueryDict)-> Response:
        return self.client.get("/api/v1/exercises", params = query)

    def get_exercise_api(self,exercise_id:str)-> Response:
        return self.client.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request:CreateExercisesRequestDict)-> Response:
        return self.client.post("/api/v1/exercises", json = request)

    def update_exercise_api(self,exercise_id: str, request: UpdateExerciseRequestDict)-> Response:
        return self.client.patch(f"/api/v1/exercises{exercise_id}", json = request)

    def delete_exercise_api(self,exercises_id:str)-> Response:
        return self.client.delete(f"/api/v1/exercises/{exercises_id}")


    def get_exercises(self,query:GetExercisesQueryDict)->GetExercisesResponseDict:
        response =  self.get_exercises_api(query)
        return response.json()
    def get_exercise(self, exercise_id:str)-> GetExerciseResponseDict:
        response = self.delete_exercise_api(exercise_id)
        return response.json()
    def create_exercise(self, request:CreateExercisesRequestDict)->GetExerciseResponseDict:
        response = self.create_exercise_api(request)
        return  response.json()
    def update_exercise(self, exercise_id:str, request:UpdateExerciseRequestDict)-> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id,request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict)-> ExercisesClient:
    return ExercisesClient(client = get_private_http_client(user))
