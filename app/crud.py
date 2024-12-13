from sqlalchemy.orm import Session
from . import models, schemas

def create_email_log(db: Session, email_log: schemas.EmailRequest):
    db_email_log = models.EmailLog(recipient=email_log.recipient, content=email_log.content, status="sent")
    db.add(db_email_log)
    db.commit()
    db.refresh(db_email_log)
    return db_email_log
