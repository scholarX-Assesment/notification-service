from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Email Service Up and Running"}

def test_send_email():
    response = client.post("/send-email/", json={"recipient": "pramodyalakmina@gmail.com", "content": "Hello, World!"})
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}

def test_send_bulk_email():
    response = client.post("/send-bulk-email/", json={"recipients": ["pramodyalakmina@gmail.com", "pramodyalakmina@gmail.com"], "content": "Hello, Everyone!"})
    assert response.status_code == 200
    assert response.json() == {"message": "Bulk emails sent successfully"}
