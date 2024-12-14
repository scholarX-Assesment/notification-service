# Email Notification Service

## Overview
The Email Notification Service is a FastAPI-based service that provides endpoints to send individual and bulk emails. It is designed to be simple and easy to integrate with other services.

## Features
- Send individual emails
- Send bulk emails
- Easy to set up and use

## Requirements
- Python 3.7+
- FastAPI
- SQLAlchemy
- A configured SMTP server for sending emails

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/notification-service.git
cd notification-service
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database
Update the `DATABASE_URL` in the `app/database.py` file to point to your database.

### 5. Configure the SMTP server
Update the SMTP settings in the `app/email.py` file with your SMTP server details.

### 6. Run the application
```bash
uvicorn main:app --reload
```

The service will be available at `http://127.0.0.1:8000`.

## API Documentation
For detailed API documentation, refer to the [API-docs.md](./API-docs.md) file.

## Contact
For any questions or issues, please contact support at support@example.com.
