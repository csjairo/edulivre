import enum
from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Enum as SAEnum
from database import Base

class GradeLevel(str, enum.Enum):
    FUNDAMENTAL = 'Fundamental'
    MEDIO = 'Médio'
    SUPERIOR = 'Superior'

class Student(Base):
    __tablename__ = "student"

    uuid = Column(UUID(as_uuid=True), ForeignKey("user.uuid"), primary_key=True)

    grade_level = Column(
        SAEnum(GradeLevel, name="grade_type", create_type=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False
    )
    interests = Column(Text)

    user = relationship("User", back_populates="student")
