# Email Notification Service API Documentation

## Overview
The Email Notification Service provides endpoints to send individual and bulk emails. This document describes the available endpoints, their parameters, and expected responses.

## Endpoints

### 1. Root
**Endpoint:** `/`

**Method:** `GET`

**Description:** Returns a message indicating that the email service is up and running.

**Response:**
- `200 OK` - Service is running.
```json
{
  "message": "Email Service Up and Running"
}
```

### 2. Send Email
**Endpoint:** `/send-email/`

**Method:** `POST`

**Description:** Sends an email to a specified recipient.

**Request Body:**
```json
{
  "recipient": "string",
  "content": "string"
}
```

**Response:**
- `200 OK` - Email sent successfully.
- `400 Bad Request` - Invalid request parameters.
- `500 Internal Server Error` - Server error.

**Response Body:**
```json
{
  "message": "Email sent successfully"
}
```

### 3. Send Bulk Email
**Endpoint:** `/send-bulk-email/`

**Method:** `POST`

**Description:** Sends emails to multiple recipients.

**Request Body:**
```json
{
  "recipients": ["string"],
  "content": "string"
}
```

**Response:**
- `200 OK` - Bulk emails sent successfully.
- `400 Bad Request` - Invalid request parameters.
- `500 Internal Server Error` - Server error.

**Response Body:**
```json
{
  "message": "Bulk emails sent successfully"
}
```

## Error Handling
All error responses will include a JSON object with an `error` field describing the issue.

**Example Error Response:**
```json
{
  "error": "string"
}
```

## Authentication
Currently, the endpoints do not require authentication. However, it is recommended to implement authentication for production use.

## Contact
For any questions or issues, please contact support at support@example.com.
