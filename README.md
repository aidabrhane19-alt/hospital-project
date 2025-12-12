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

Patient Management:

Add new patient details (name, age, gender, contact info, address, medical history).

Update or delete patient records.

Search and retrieve patient information.

Doctor Management:

Add, update, or delete doctor details (name, specialization, availability, contact info).

Assign doctors to patients.

View doctor schedules and appointments.

Appointment Management:

Schedule new appointments (patient ID, doctor ID, date, time, purpose).

Update or cancel appointments.

View upcoming appointments for patients and doctors.

Medical Records: Maintain patient medical history linked to both patients and doctors.

Staff Management: Add and manage staff details (nurses, receptionists, technicians, etc.).

Technology Stack
Layer	Technology
Frontend	React.js
Backend	Django (Python)
Database	SQLite (development) / PostgreSQL (production)
Authentication	Django Auth with role-based access
Styling	CSS / TailwindCSS (if applicable)
API	RESTful API using Django REST Framework
Architecture

Frontend: React for dynamic and responsive user interfaces.

Backend: Django handles authentication, database management, API endpoints, and role-based logic.

Database: Stores patient, doctor, staff, appointments, and medical record information.

Communication: REST API connects frontend and backend.

Installation

Clone the repository

githttps://github.com/aidabrhane19-alt/hospital-project
cd Hospital-Management-System

Set up Python backend (Django)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Set up React frontend

cd frontend
npm install
npm start


Open your browser:

Backend API: http://127.0.0.1:8000/

Frontend UI: http://localhost:3000/

Usage

Admin can manage patients, doctors, staff, and appointments.

Doctors can view schedules, manage appointments, and update medical records.

Receptionists can schedule appointments and manage patient information.

Pharmacists can access prescription-related data if extended.

Contributors

birtukan,birtquan,ayda– Backend (Django, REST API)

mleat, adanech– Frontend (React)

Team members – birtquan tetemke, birtukan  g/kidan, ayda brhane, mleat aregawi, adanech mokenen

License

This project is licensed under the MIT License – see the LICENSE
 file for details.
