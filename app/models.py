from sqlalchemy import Column, Integer, String
from .database import Base

class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)
    recipient = Column(String, index=True)
    content = Column(String)
    status = Column(String)
