from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, email, database
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notification Service APIs", version="1.0")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Email Service Up and Running"}

@app.post("/send-email/")
def send_email(email_request: schemas.EmailRequest, db: Session = Depends(get_db)):
    email.send_email(email_request.recipient, email_request.content)
    return {"message": "Email sent successfully"}

@app.post("/send-bulk-email/")
def send_bulk_email(bulk_email_request: schemas.BulkEmailRequest, db: Session = Depends(get_db)):
    for recipient in bulk_email_request.recipients:
        email.send_email(recipient, bulk_email_request.content)
    return {"message": "Bulk emails sent successfully"}
