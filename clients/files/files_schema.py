from pydantic import BaseModel,Field,HttpUrl


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestShema(BaseModel):
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    file: FileSchema