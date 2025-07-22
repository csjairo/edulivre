from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from database import Base

class Teacher(Base):
    __tablename__ = "teacher"

    uuid = Column(UUID(as_uuid=True), ForeignKey("user.uuid"), primary_key=True)

    degree = Column(Text)
    specialties = Column(Text)

    user = relationship("User", back_populates="teacher")
