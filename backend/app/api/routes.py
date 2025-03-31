from fastapi import APIRouter
from app.services.grader import grade_project
from app.models.schemas import ProjectIdea, GradingResponse

router = APIRouter()

@router.post("/grade", response_model=GradingResponse)
def grade_project_idea(project: ProjectIdea):
    """Endpoint"""
    return grade_project(project)
