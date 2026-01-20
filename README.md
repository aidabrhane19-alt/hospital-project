Hospital Management System

A full-stack web application for managing hospital operations efficiently. The system provides role-based access and allows hospitals to manage patients, doctors, staff, appointments, and medical records through a secure and user-friendly interface.

Table of Contents

Project Overview

Features

Technology Stack

Architecture

Installation

Usage

Contributors

License

Project Overview

The Hospital Management System is designed to streamline hospital workflows and improve healthcare service quality. It centralizes patient records, doctor schedules, appointments, and staff management, ensuring accurate data, efficient processes, and secure access based on user roles.

Features

Role-Based Access: Admin, Doctor, Receptionist, Pharmacist.

Authentication: Login and logout functionality.

Patient Management

Add new patient details (name, age, gender, contact info, address, medical history).

Update or delete patient records.

Search and retrieve patient information.

Doctor Management

Add, update, or delete doctor details (name, specialization, availability, contact info).

Assign doctors to patients.

View doctor schedules and appointments.

Appointment Management

Schedule new appointments (patient ID, doctor ID, date, time, purpose).

Update or cancel appointments.

View upcoming appointments for patients and doctors.

Medical Records

Maintain patient medical history linked to both patients and doctors.

Staff Management

Add and manage staff details (nurses, receptionists, technicians, etc.).

Technology Stack
Layer	Technology
Frontend	Django Templates, HTML, CSS
Backend	Django (Python)
Database	SQLite (development) / PostgreSQL (production)
Authentication	Django Auth with role-based access
Styling	CSS / TailwindCSS (if applicable)
API	RESTful API using Django REST Framework
Architecture

Frontend: Django templates for dynamic and responsive user interfaces.

Backend: Django handles authentication, database management, API endpoints, and role-based logic.

Database: Stores patient, doctor, staff, appointments, and medical record information.

Communication: Backend serves HTML pages directly; REST API supports additional integrations if needed.

Installation
Clone the repository
git clone https://github.com/aidabrhane19-alt/hospital-project.git
cd Hospital-Management-System

Set up Python backend (Django)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Open your browser

Backend: http://127.0.0.1:8000/

Note: No separate frontend framework is used; all user interfaces are served via Django templates.

Usage

Admin: Manage patients, doctors, staff, and appointments.

Doctor: View schedules, manage appointments, and update medical records.

Receptionist: Schedule appointments and manage patient information.

Pharmacist: Access prescription-related data.

Contributors

Backend (Django, REST API): Birtukan, Birtquan, Ayda

Team Members: Birtquan Tetemke, Birtukan G/Kidan, Ayda Brhane, Mleat Aregawi, Adanech Mokenen

License

This project is licensed under the MIT License see the LICENSE
 file for details.

