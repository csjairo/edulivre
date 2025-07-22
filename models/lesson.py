import uuid
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class Lesson(Base):
    __tablename__ = "lesson"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    class_type = Column(String(50))
    status = Column(String(50))
    recording_url = Column(Text)
    teacher_uuid = Column(UUID(as_uuid=True), ForeignKey("teacher.uuid"), nullable=False)
    workshop_uuid = Column(UUID(as_uuid=True), ForeignKey("workshop.uuid"), nullable=False)

    teacher = relationship("Teacher", back_populates="lessons")
    workshop = relationship("Workshop", back_populates="lessons")
