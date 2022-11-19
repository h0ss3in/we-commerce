from fastapi import APIRouter, Depends

from app.dependencies import CheckoutHandler

router = APIRouter(
    prefix="/checkout",
    tags=["checkout"],
    responses={404: {"detail": "Not found"}},
)


@router.post("/")
async def create_checkout(checkout: CheckoutHandler = Depends()):
    checkout.create()
    return {
        "price": checkout.total_price
    }
