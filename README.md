# Student Management System API
Built using Django and Django REST Framework

A RESTful API for managing student records with full CRUD functionality using Django and Django REST Framework.

---

## Live Demo

**Live Demo:** [Click here](https://student-management-system-api-8nko.onrender.com/api/students/)

> Note: Free tier — may take 50 seconds to wake up on first request.

---

## Overview

This project demonstrates backend API development using Django REST Framework. It follows a clean architecture with models, serializers, and views to implement RESTful endpoints.

The API allows creation, retrieval, updating, and deletion of student records stored in a relational database.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default Django database)
- Whitenoise
- Gunicorn
- Render (deployment)


---

## Features

- Create student record
- Retrieve all students
- Retrieve student by ID
- Update student details
- Delete student record
- Model-based database integration
- DRF serializers for validation
- RESTful API design

---

## Project Structure
```
student-management-system-api/
├── config/              # Django project settings
├── manage.py
├── students/            # App containing models, views, serializers
└── README.md
```
---

## Installation

Clone the repository:
```
git clone https://github.com/Sudipta7-ops/student-management-system-api.git
cd student-management-system-api
```
Create virtual environment:
```
python -m venv venv
```
Activate environment (Windows):
```
venv\Scripts\activate
```
Install dependencies:
```
pip install -r requirements.txt
```
---

## Database Setup
```
python manage.py makemigrations  
python manage.py migrate
```
---

## Run the Server
```
python manage.py runserver
```
Server will run at:

http://127.0.0.1:8000/

---

## API Endpoints
```
GET     /api/students/  
GET     /api/students/<id>/  
POST    /api/students/  
PUT     /api/students/<id>/  
DELETE  /api/students/<id>/
```
---

## Example Request Body
```
{
    "name": "John Doe",
    "age": 21,
    "email": "john@example.com"
}
```
---

## Learning Outcomes

- RESTful API development
- Django project architecture
- Model-Serializer-View pattern
- Database migrations
- API validation using DRF

---

## Future Improvements

- JWT authentication
- Pagination and filtering
- Docker support

---

 ## Author

**Sudipta Barik** — [LinkedIn](https://linkedin.com/in/sudipta-barik) | [GitHub](https://github.com/Sudipta7-ops)
"@

---