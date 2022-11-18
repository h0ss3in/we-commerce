from fastapi import APIRouter

router = APIRouter(
    prefix="/checkout",
    tags=["checkout"],
    responses={404: {"detail": "Not found"}},
)


@router.post("/")
async def checkout():
    return {
        "price": 360
    }
