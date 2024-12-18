from fastapi import APIRouter, Depends
from pydantic import UUID4
from app.base.dao import RoofsDAO
from app.base.schemas import RoofRequest, RoofResponse
from app.exceptions import RoofNotFound
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/base", tags=["Base"])

@router.post("/roofs_base", description="Добавление покрытия в библиотеку")
async def add_roof_base(roof: RoofRequest,
                        user: Users = Depends(get_current_user)) -> RoofResponse:
    result = await RoofsDAO.add(name=roof.name,
                                 type=roof.type,
                                 overall_width=roof.overall_width,
                                 useful_width=roof.useful_width,
                                 overlap=roof.overlap,
                                 max_length=roof.max_length)
    return RoofResponse(roof_id=result.id, 
                        roof_name=result.name,
                        roof_type=result.type,
                        roof_overall_width=result.overall_width,
                        roof_useful_width=result.useful_width,
                        roof_overlap=result.overlap,
                        roof_max_length=result.max_length)

@router.get("/roofs_base", description="Получение покрытий из библиотеки")
async def get_roof_base(user: Users = Depends(get_current_user)) -> list[RoofResponse]:
    results = await RoofsDAO.find_all()
    if not results:
        raise RoofNotFound
    return [
        RoofResponse(roof_id=result.id, 
                        roof_name=result.name,
                        roof_type=result.type,
                        roof_overall_width=result.overall_width,
                        roof_useful_width=result.useful_width,
                        roof_overlap=result.overlap,
                        roof_max_length=result.max_length)
                        for result in results
    ]

@router.delete("/roofs_base", description="Удаление покрытия из библиотеки")
async def delete_roof_base(roof_id: UUID4,
                          user: Users = Depends(get_current_user)) -> None:
    await RoofsDAO.delete_(model_id=roof_id)