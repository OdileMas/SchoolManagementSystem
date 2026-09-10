# School Management System

A Django-based backend for managing the core day-to-day records of a school:
students, teachers, classes, subjects, exams, grades, and attendance.

---

## About the Project

This system is designed to bring a school's academic records into one
structured, relational database — replacing scattered spreadsheets or paper
records with a single source of truth. It manages:

- Student and teacher accounts
- Classes (grades/sections) and the subjects taught within them
- Exams and the grades students receive
- Daily attendance records

The goal is a backend that's accurate, easy to query, and ready to support a
future front-end (web dashboard, mobile app, or admin reports) without
changing the underlying data structure.

## Core Features (Planned)

- Role-based accounts for **admins**, **teachers**, and **students**
- Class and subject management, with teachers assigned to subjects
- Exam creation and grade recording per student, per subject
- Daily attendance tracking per student, per class
- Referential integrity enforced via foreign keys and cascading deletes

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| Framework | Django |
| Database | PostgreSQL (SQLite for local development) |
| Auth | Custom Django `User` model, role-based (admin/teacher/student) |
| Planned | Django REST Framework (API layer) |

## Project Structure


school_system/
├── school_system/        # project settings, root urls
├── accounts/               # custom User model (role: admin/teacher/student)
├── students/                # Student profile
├── teachers/                # Teacher profile
├── academics/               # Class and Subject models
├── attendance/               # Attendance records
├── exams/                    # Exam and Grade models
├── manage.py
├── requirements.txt
└── .gitignore


## Data Model Overview

| App | Models | Purpose |
|---|---|---|
| `accounts` | `User` | Shared login, role-based (admin/teacher/student) |
| `students` | `Student` | Student profile, linked one-to-one to `User` |
| `teachers` | `Teacher` | Teacher profile, linked one-to-one to `User` |
| `academics` | `Class`, `Subject` | School structure: grades/sections and subjects taught |
| `attendance` | `Attendance` | Daily record of a student's presence per class |
| `exams` | `Exam`, `Grade` | Exams held per subject/class, and the grades students receive |

**Key relationships (to be finalized as models are written)**
- A class has many students, and many subjects taught within it
- A teacher teaches many subjects/classes
- An exam belongs to a subject and a class; a grade belongs to a student and an exam
- Attendance links a student to a class on a given date

## Getting Started

### Prerequisites
- Python 3.10+
- pip
- PostgreSQL (only required for production/staging — local dev can use SQLite)
- Git

### 1. Clone the repository

git clone https://github.com/OdileMas/SchoolManagementSystem
cd SchoolManagementSystem
cd school_management


### 2. Create and activate a virtual environment

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Configure environment variables
Create a `.env` file in the project root (never commit this file):

SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

For production/staging with PostgreSQL, replace `DATABASE_URL` with:

DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME


### 5. Apply migrations

python manage.py makemigrations
python manage.py migrate


### 6. Create a superuser (for Django admin access)

python manage.py createsuperuser

### 7. Run the development server

python manage.py runserver

Visit "http://127.0.0.1:8000/admin/" to access the Django admin panel.

## Dependencies

See `requirements.txt` for the exact pinned versions. Core packages expected
in this project:
- `django`
- `djangorestframework` (API layer)
- `psycopg2-binary` (PostgreSQL driver)
- `python-decouple` or `django-environ` (environment variable management)

> If `requirements.txt` isn't committed yet, generate it from your active
> virtual environment with:

> pip freeze > requirements.txt


## Branching & Workflow

Branches follow the pattern `type/short-description`, e.g.
`feature/student-model`. Each feature is developed on its own branch and
merged into `main` via pull request.

## Project Status

 **Early scaffold stage.** App structure is in place; models for each app
are being written incrementally, one feature/branch at a time.

## License

_To be determined._