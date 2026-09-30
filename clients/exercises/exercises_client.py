from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_chema import (GetExercisesQuerySchema,CreateExerciseRequestSchema,UpdateExerciseRequestSchema,
UpdateExerciseRequestSchema,GetExerciseResponseSchema,CreateExerciseResponseSchema,UpdateExerciseResponseSchema)



class ExercisesClient(APIClient):
    def get_exercises_api(self, query:GetExercisesQuerySchema)-> Response:
        return self.client.get("/api/v1/exercises", params = query.model_dump())

    def get_exercise_api(self,exercise_id:str)-> Response:
        return self.client.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request:CreateExerciseRequestSchema)-> Response:
        return self.client.post("/api/v1/exercises", json = request.model_dump(by_alias=True))

    def update_exercise_api(self,exercise_id: str, request: UpdateExerciseRequestSchema)-> Response:
        return self.client.patch(f"/api/v1/exercises{exercise_id}", json = request.model_dump(by_alias=True))

    def delete_exercise_api(self,exercises_id:str)-> Response:
        return self.client.delete(f"/api/v1/exercises/{exercises_id}")


    def get_exercises(self,query:GetExercisesQuerySchema)->GetExerciseResponseSchema:
        response =  self.get_exercises_api(query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id:str)-> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request:CreateExerciseRequestSchema)->CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return  CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id:str, request:UpdateExerciseRequestSchema)-> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id,request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema)-> ExercisesClient:
    return ExercisesClient(client = get_private_http_client(user))
