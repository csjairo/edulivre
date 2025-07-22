# models/teacher.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, index=True)
    degree = Column(Text)
    specialties = Column(Text)

    # Chave estrangeira para o uuid do usuário
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("user.uuid"), unique=True, nullable=False)

    # Relacionamento com o modelo User
    user = relationship("User", back_populates="teacher")
