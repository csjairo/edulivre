import uuid
from sqlalchemy import Column, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class Participate(Base):
    __tablename__ = "participate"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_uuid = Column(UUID(as_uuid=True), ForeignKey("student.uuid"), nullable=False)
    workshop_uuid = Column(UUID(as_uuid=True), ForeignKey("workshop.uuid"), nullable=False)
    enrolled_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    student = relationship("Student", back_populates="workshops")
    workshop = relationship("Workshop", back_populates="students")
