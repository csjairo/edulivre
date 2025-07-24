from fastapi import FastAPI
from database import Base, engine
from routers import (
    participate_router, user_router,
    student_router, workshop_router,
    frequency_router, history_router,
    teacher_router, lesson_router
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="EduLivre API")

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(workshop_router.router)
app.include_router(participate_router.router)
app.include_router(lesson_router.router)
app.include_router(frequency_router.router)
app.include_router(history_router.router)
