# Advanced-Of-Data-Base-HomeWork-5

---
---
---

Lorestan University Database API

A FastAPI project for managing a database of students, lecturers, courses, course registrations, and presented courses for Lorestan University. It integrates with MongoDB and provides CRUD operations for the database.
Features

```bash
    FastAPI framework for building robust and fast APIs.
    MongoDB for data storage.
    CRUD Operations for Students, Lecturers, Courses, Course Registrations, and Presented Courses.
    Validation using Pydantic models.
    Alembic for database migrations.
```

Requirements

To run this project, ensure you have the following installed:

```bash
    Python (3.8 or higher)
    MongoDB Atlas or local MongoDB instance
    Virtual Environment (optional, but recommended)
    FastAPI and supporting libraries
    SQLAlchemy for database modeling
    Alembic for migrations
```

Setup and Installation

```bash
    Clone this repository:
```
 ---

 ```bash

git clone https://github.com/babakyousefian/Advanced-Of-Data-Base-HomeWork-5.git
cd Advanced-Of-Data-Base-HomeWork-5

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

Install dependencies:

```python
pip install -r requirements.txt
```

Configure MongoDB:

```bash
    Update the MongoDB connection URI in the codes.txt file:

    uri = "your-mongo-connection-uri"
```

Run the application:

```bash

    uvicorn main:app --reload

    By default, the application runs at http://127.0.0.1:8000.
```

Endpoints

Here is a summary of the available endpoints:
1. Read All Data

GET /Data/Read/

Description: Fetch all data (students, lecturers, courses, registrations, presented courses) from the database.
2. Create Records

POST /Data/Create/

Description: Add records for Students, Lecturers, Courses, Registrations, and Presented Courses.

Payload Example:

```python

{
  "Stu": {
    "FName": "John",
    "LName": "Doe",
    "Father": "Smith",
    "Birth": "1995-01-01",
    "IDS": "12345678901",
    "BornCity": "Lorestan",
    "Address": "123 University Street",
    "PostalCode": "12345",
    "CPhone": "09123456789",
    "HPhone": "02112345678",
    "Department": "Computer Science",
    "Major": "AI",
    "Married": false,
    "ID": "12345678901"
  },
  "lec": {...},
  "cor": {...},
  "cr": {...},
  "pres": {...}
}

```

3. Update Records

PUT /Data/Update/

Description: Update existing data for students, lecturers, or courses.

Payload Example:

```bash

{
  "s_id": 1,
  "l_id": 2,
  "Stu": {...},
  "lec": {...}
}

```

4. Delete Records

DELETE /Data/Delete/

Description: Delete specified records by their IDs.

Query Parameters Example:

```bash

{
  "s_id": 1,
  "l_id": 2
}

```

Models
Student

    FName, LName, Father (string, length 1–10)
    Birth (datetime)
    IDS (string, length 11)
    PostalCode (integer, 5 digits)

Lecturer

    FName, LName (string, length 1–10)
    Department (string)
    Major

Course

    CName (string)
    Credit (integer)

CourseRegister

    CName, Department

PresentedCourses

    CName, FName, LName

Testing Endpoints

Use a tool like Postman or cURL for testing API endpoints.
Database Migrations (SQLAlchemy + Alembic)


Initialize Alembic:

```bash

alembic init alembic

```

Generate a migration:

```bash

alembic revision --autogenerate -m "Initial migration"

```

Apply migrations:

```bash

    alembic upgrade head
```


License

This project is licensed under the MIT License.

This document serves as a comprehensive guide to setting up and using the FastAPI Lorestan University database application.



---
---
---

# Lorestan University Database API

A FastAPI project designed to manage a database for Lorestan University, including Students, Lecturers, Courses, Course Registrations, and Presented Courses. This project uses MongoDB as its primary database and provides a robust API for CRUD operations with integrated validation.

---

## Features

- **FastAPI Framework**: A high-performance, modern web framework for building APIs.
- **MongoDB Atlas Integration**: Cloud database support for scalability and reliability.
- **CRUD Operations**: Fully implemented Create, Read, Update, Delete functionalities.
- **Validation**: Enforced through Pydantic models for data accuracy.
- **Data Serialization**: Convert database objects into easily consumable formats.
- **Alembic Migrations**: Manage changes to SQL database schemas.

---

## Project Structure

```
.
├── main.py              # Entry point for the FastAPI application
├── database/            # Contains database connection and setup files
├── models/              # Pydantic and SQLAlchemy models for schema definition
├── routers/             # API routers to handle different endpoints
├── alembic/             # Alembic migration files for schema version control
├── README.md            # Documentation for the project
├── requirements.txt     # Python dependencies
```

---

## Prerequisites

### Install the Following:

- Python 3.8 or higher
- MongoDB Atlas account or local MongoDB setup
- Pip (Python package installer)
- Optionally, Docker for containerization

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MongoDB

Update the connection URI in the relevant file:

```python
uri = "your-mongo-connection-uri"
```

---

## Running the Application

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. The API will be accessible at:

   ```
   http://127.0.0.1:8000
   ```

---

## API Endpoints

### Base URL: `http://127.0.0.1:8000`

### 1. Read All Data

**Endpoint**: `/Data/Read/`

**Method**: `GET`

Fetch all records (students, lecturers, courses, course registrations, and presented courses).

### 2. Create Data

**Endpoint**: `/Data/Create/`

**Method**: `POST`

Add a new record for students, lecturers, courses, course registrations, and presented courses.

**Payload Example**:
```json
{
    "Stu": {
        "FName": "John",
        "LName": "Doe",
        "Father": "Smith",
        "Birth": "1995-01-01",
        "IDS": "12345678901",
        "BornCity": "Lorestan",
        "Address": "123 University Street",
        "PostalCode": "12345",
        "CPhone": "09123456789",
        "HPhone": "02112345678",
        "Department": "Computer Science",
        "Major": "AI",
        "Married": false,
        "ID": "12345678901"
    }
}
```

### 3. Update Data

**Endpoint**: `/Data/Update/`

**Method**: `PUT`

Update an existing record for students, lecturers, courses, course registrations, or presented courses.

**Payload Example**:
```json
{
    "s_id": 1,
    "Stu": {
        "FName": "Jane",
        "LName": "Doe"
    }
}
```

### 4. Delete Data

**Endpoint**: `/Data/Delete/`

**Method**: `DELETE`

Delete records by IDs for students, lecturers, or other entities.

**Query Example**:
```json
{
    "s_id": 1,
    "l_id": 2
}
```

### 5. Test Endpoint

**Endpoint**: `/Items/Details/hello/`

**Method**: `GET`

Returns a simple response:
```json
{
    "your output is": "hi there...!!!"
}
```

---

## Database Models

The following entities are modeled in the project:

### **Student**

| Field       | Type   | Constraints          |
|-------------|--------|----------------------|
| FName       | String | Length 1-10          |
| LName       | String | Length 1-10          |
| Birth       | Date   | Valid date           |
| IDS         | String | Length 11           |
| ...         | ...    | ...                  |

### **Lecturer**

| Field       | Type   | Constraints          |
|-------------|--------|----------------------|
| FName       | String | Length 1-10          |
| LName       | String | Length 1-10          |
| Department  | String | Not Null             |
| ...         | ...    | ...                  |

### **Course**

| Field       | Type   | Constraints          |
|-------------|--------|----------------------|
| CName       | String | Length 1-25          |
| Credit      | Int    | 1-4                  |
| Department  | String | Length 1-51          |

---

## Testing

Use tools like **Postman**, **cURL**, or **HTTPie** for testing the endpoints. For example:

### Test Endpoint `/Data/Read/`

```bash
curl -X GET http://127.0.0.1:8000/Data/Read/
```

---

## Database Migration (SQLAlchemy + Alembic)

1. Initialize Alembic:

   ```bash
   alembic init alembic
   ```

2. Generate a new migration:

   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

3. Apply migrations:

   ```bash
   alembic upgrade head
   ```

---

## License

This project is licensed under the MIT License.

---

- @Author : babak yousefian


