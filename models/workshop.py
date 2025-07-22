import uuid
from sqlalchemy import Column, String, Text, Integer, TIMESTAMP, Interval, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class Workshop(Base):
    __tablename__ = "workshop"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    category = Column(String(100))
    address = Column(Text)
    description = Column(Text)
    capacity = Column(Integer)
    start_date = Column(TIMESTAMP, nullable=False)
    end_date = Column(TIMESTAMP, nullable=False)
    duration = Column(Interval)
    teacher_uuid = Column(UUID(as_uuid=True), ForeignKey("teacher.uuid"), nullable=False)

    teacher = relationship("Teacher", back_populates="workshops")
    students = relationship("Participate", back_populates="workshop")
