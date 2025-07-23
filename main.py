from fastapi import FastAPI
from database import Base, engine
from routers import participate_router, user_router
from routers import student_router, workshop_router
from routers import frequency_router, history_router
from routers import teacher_router, lesson_router

app = FastAPI(title="EduLivre API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(workshop_router.router)
app.include_router(participate_router.router)
app.include_router(lesson_router.router)
app.include_router(frequency_router.router)
app.include_router(history_router.router)
