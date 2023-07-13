from fastapi import APIRouter, Depends

from src import schemas, deps
from src.repo.item_repo import ItemRepo

router = APIRouter()


@router.get("/")
async def read_items(
        item_repo: ItemRepo = Depends(deps.get_repo(ItemRepo)),
) -> list[schemas.ItemWithUser]:
    """
    Retrieve items.
    """
    items = await item_repo.get_items_with_user()
    return items
