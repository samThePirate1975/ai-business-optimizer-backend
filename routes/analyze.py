from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def analyze_business():
    return {"message": "Endpoint pour analyser un business et proposer des optimisations"}
