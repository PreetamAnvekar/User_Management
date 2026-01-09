# User & Task Management API

A simple Django REST API built using Django Rest Framework (DRF) and PostgreSQL to manage users and their tasks.

---

## Tech Stack

- Python 3.9+
- Django
- Django REST Framework
- PostgreSQL
- psycopg2
- python-dotenv

---

## Setup Instructions

### 1. Clone the Project
```bash
git clone <repository-url>
cd user_management
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## PostgreSQL Configuration

### 1. Create Database
```sql
CREATE DATABASE user_management_db;
```

### 2. Create `.env` File in Project Root

```env
DB_NAME=user_management_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your-secret-key
```

Ensure PostgreSQL service is running before starting the project.

---

## Migration Commands

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

Start the server:
```bash
python manage.py runserver
```

---

## API Endpoints & Sample Requests

### Create User
**POST** `/users/`
```json
{
  "username": "abc",
  "email": "abc@gmail.com"
}
```

---

### List Users
**GET** `/users/`

---

### Create Task
**POST** `/tasks/`
```json
{
  "title": "OCR",
  "description": "Fetch Text from PDF",
  "status": "Pending",
  "user": 1
}
```

---

### List All Tasks
**GET** `/tasks/`

---

### Filter Tasks by Status
**GET**
```
/tasks/?status=Completed
```

---

### Get Task Details
**GET** `/tasks/1/`

---

### Update Task
**PUT** `/tasks/1/`
```json
{
  "title": "OCR",
  "description": "Fetch Text from PDF",
  "status": "Completed",
  "user": 1
}
```

---

### Delete Task
**DELETE** `/tasks/1/`

---

## Django Admin Panel

Access the admin panel:
```
http://127.0.0.1:8000/admin/
```

Admin can manage:
- Users
- Tasks

---

