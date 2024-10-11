from fastapi import APIRouter, Depends
from app.base.dao import RoofsDAO
from app.base.schemas import RoofRequest, RoofResponse
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/base", tags=["Base"])

@router.post("/roofs_base", description="Добавление покрытия в библиотеку")
async def add_roof_base(roof: RoofRequest,
                        user: Users = Depends(get_current_user)) -> RoofResponse:
    result = await RoofsDAO.add(name=roof.name,
                                 type=roof.type,
                                 price=roof.price,
                                 overall_width=roof.overall_width,
                                 useful_width=roof.useful_width,
                                 overlap=roof.overlap,
                                 material=roof.material,
                                 color=roof.color,
                                 min_length=roof.min_length,
                                 max_length=roof.max_length)
    return RoofResponse(roof_id=result.id, 
                        roof_name=result.name,
                        roof_type=result.type,
                        roof_price=result.price,
                        roof_overall_width=result.overall_width,
                        roof_useful_width=result.useful_width,
                        roof_overlap=result.overlap,
                        roof_material=result.material,
                        roof_color=result.color,
                        roof_min_length=result.min_length,
                        roof_max_length=result.max_length)
