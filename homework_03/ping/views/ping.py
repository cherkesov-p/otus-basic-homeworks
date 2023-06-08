from fastapi import APIRouter
from fastapi import status

router = APIRouter(
    tags=["Ping"]
)


@router.get("/ping/", status_code=status.HTTP_200_OK)
def ping() -> dict:
    return {
        "message": "pong",
    }
