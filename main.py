"""
test apikey
"""
from fastapi import Depends, FastAPI, Request, Security, status
from fastapi.exceptions import HTTPException
from fastapi.security.api_key import APIKeyHeader

app = FastAPI()

API_KEY_NAME = "my_api_key_name"
API_KEY = "my_api_key"

api_key_header_obj = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    api_key_header: str = Security(api_key_header_obj),
):
    """
    validate the api key
    """

    if api_key_header == API_KEY:
        return api_key_header

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )


@app.post("/")
async def root(
    request: Request,
    api_key=Depends(get_api_key),
):
    """
    test api key
    """

    print(await request.json())

    return {
        "message": api_key,
    }
