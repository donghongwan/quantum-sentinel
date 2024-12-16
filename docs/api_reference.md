# API Documentation

## Overview
This document provides a reference for the Quantum Sentinel API, detailing available endpoints and their usage.

## Authentication
All API requests require authentication. Use the following method to authenticate:

- **Endpoint**: `/api/auth/login`
- **Method**: POST
- **Request Body**:
  ```json
  1 {
  2   "username": "your_username",
  3   "password": "your_password"
  4 }
  ```

## Endpoints

1. Get User Information
- **Endpoint**: /api/users/{id}
- **Method**: GET
- **Description**: Retrieve information about a specific user.
- **Response**:
```json
1 {
2   "id": "user_id",
3   "username": "user_name",
4   "email": "user_email"
5 }
```

2. Create New User
- **Endpoint**: /api/users
- **Method**: POST
- **Request Body**:
```json
1 {
2   "username": "new_user",
3   "password": "user_password",
4   "email": "user_email"
5 }
```

3. Update User Information
- **Endpoint**: /api/users/{id}
- **Method**: PUT
- **Request Body**:
```json
1 {
2   "email": "new_email"
3 }
```

## Error Handling
Common error responses and their meanings.
