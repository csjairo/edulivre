import uuid
from sqlalchemy import Column, TIMESTAMP, ForeignKey, Enum as SAEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
import enum

class AttendanceStatus(str, enum.Enum):
    PRESENTE = "Presente"
    AUSENTE = "Ausente"
    JUSTIFICADO = "Justificado"

class Frequency(Base):
    __tablename__ = "frequency"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_uuid = Column(UUID(as_uuid=True), ForeignKey("student.uuid"), nullable=False)
    lesson_uuid = Column(UUID(as_uuid=True), ForeignKey("lesson.uuid"), nullable=False)
    status = Column(
        SAEnum(AttendanceStatus, name="attendance_status", create_type=False, values_callable=lambda obj: [e.value for e in obj]),
        nullable=False
    )
    recorded_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

    student = relationship("Student")
    lesson = relationship("Lesson")
