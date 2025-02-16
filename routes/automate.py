from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def automate_task():
    return {"message": "Endpoint pour automatiser une tâche avec l'IA"}
