from fastapi import FastAPI
from database import Base, engine
from routers import user_router, teacher_router, student_router

app = FastAPI(title="EduLivre API")

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
