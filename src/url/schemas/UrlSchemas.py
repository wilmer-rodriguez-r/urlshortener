from pydantic import BaseModel, HttpUrl, ConfigDict

class Url(BaseModel):
    id: None | str = None
    original_url: HttpUrl
    short_url: HttpUrl
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "original_url": "http://example.com/somelargetextqwertyuiop",
                "short_url": "http://name_api/shorturl",
            }
        },
    )

class CreateUrl(BaseModel):
    original_url: HttpUrl
    model_config = ConfigDict(
         json_schema_extra={
            "example": {
                "original_url": "http://example.com/somelargetextqwertyuiop"
            }
        },
    )