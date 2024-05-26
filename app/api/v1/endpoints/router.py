# app/api/v1/router.py
from fastapi import APIRouter
from app.api.v1.endpoints import access, agents, auth, configuration, files, hashlists, tasks, users

api_router = APIRouter()
api_router.include_router(access.router, prefix="/access", tags=["access"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(configuration.router, prefix="/configuration", tags=["configuration"])
api_router.include_router(files.router, prefix="/files", tags=["files"])
api_router.include_router(hashlists.router, prefix="/hashlists", tags=["hashlists"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
