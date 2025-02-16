from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def optimize_content():
    return {"message": "Endpoint pour optimiser un contenu textuel"}
